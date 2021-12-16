from rest_framework import fields, serializers
from typing import List, Dict, Optional, Union, Tuple
from pydantic.main import ModelMetaclass
from pydantic import BaseModel, create_model
from decimal import Decimal


def field_to_pydantic_args(f : fields.Field) -> Dict:
    
    """ Given a DRF Field, returns a dictionary of arguments to be passed
    to pydantic.create_model() field configs.
    """
    
    args = {
        'extra':{}
    }

    if hasattr(f, 'label'):
        args['alias']=f.label

    if hasattr(f, 'help_text'):        
        args['description']= f.help_text
        
    if hasattr(f, 'read_only'):
        args['extra']['readonly'] = f.read_only

    if hasattr(f, 'write_only'):
        args['extra']['writeonly'] = f.write_only
        
    if hasattr(f, 'format'):
        args['format'] = f.format
        
    # string fields
    if hasattr(f, 'max_length'):
        
        # Avoid clashing with ListSerializer or ListField max_length property
        
        if isinstance(f, serializers.ListSerializer):
            pass
        elif isinstance(f, fields.ListField):
            pass
        else:
            args['max_length'] = f.max_length
        
    if hasattr(f, 'min_length'):
        # Avoid clashing with ListSerializer or ListField min_length property
        if isinstance(f, serializers.ListSerializer):
            pass
        elif isinstance(f, fields.ListField):
            pass
        else:
            args['min_length'] = f.min_length

    if hasattr(f, 'uuid_format'):
        args['format'] = f.uuid_format
        
    #TODO: Handle regex field format

    # numeric fields
    if hasattr(f, 'max_value'):
        args['lt'] = f.max_value
        
    if hasattr(f, 'min_value'):
        args['gt'] = f.min_value
        
    # choice fields
    if hasattr(f, 'choices'):
        # choices attr is a list of (key, display_name) tuples.
        args['extra']['choices'] = f.choices
        
    return args
    
class SerializerConverter(BaseModel):
    
    """ Converter class to convert 
    Serializer or ListSerializer into a pydantic model
    """

    s : Union[serializers.Serializer, serializers.ListSerializer]
        
    class Config:
        arbitrary_types_allowed = True
    
    @classmethod
    def infer_field_type(cls, field : fields.Field):
        """ Classifies DRF Field types into primitive python types or 
        creates an appropriate pydantic model metaclass types if the field itself
        is a Serializer class.
        
        """
        mappings = {
            fields.BooleanField: bool,
            fields.NullBooleanField: bool,
            fields.CharField: str,
            fields.EmailField: str,
            fields.RegexField: str,
            fields.SlugField: str,
            fields.URLField: str,
            fields.UUIDField: str,
            fields.FilePathField: str,
            fields.IPAddressField: str,
            fields.IntegerField: int,
            fields.FloatField: float,
            fields.DecimalField: Decimal,
            fields.DateTimeField: str,
            fields.DateField: str,
            fields.TimeField: str,
            fields.DurationField: str,
            fields.ChoiceField: str,
            fields.MultipleChoiceField: str,
            fields.FileField: str,
            fields.ImageField: str,
            fields.ListField: List,
            fields.DictField: Dict,
            fields.HStoreField: Dict,
            fields.JSONField: str,
        }
        
        # Handle case where nested serializer is a field 
        if hasattr(field, "get_fields"):
            return cls.from_serializer(field)    

        # Handle DictField
        if type(field) == fields.DictField:
            if hasattr(field, 'child'):
                t = cls.infer_field_type(field.child)
                return Dict[str, t]
        
        return mappings.get(type(field))

    @classmethod
    def from_list_serializer(cls, s: serializers.ListSerializer) -> ModelMetaclass:
        
        """ Converts a DRF ListSerializer into a pydantic model.
        This is used when the parent serializer is a ListSerializer instead of a Serializer.
        """
        name = s.__class__.__name__
        child_model = cls.from_serializer(s.child)

        class Config:
            fields={'__root__':{}}

        if hasattr(s, 'max_length'):
            Config.fields['__root__'].update({'max_items':s.max_length})
        
        if hasattr(s, 'min_length'):
            Config.fields['__root__'].update({'min_items':s.min_length})

        model = create_model(name, __root__=(List[child_model], ...), __config__=Config)
        model.__doc__ = s.__doc__
        
        return model

    @classmethod
    def from_serializer(cls, s : serializers.Serializer) -> ModelMetaclass:

        """ Converts a DRF Serializer type into a pydantic model.
        """

        name = s.__class__.__name__
            
        create_model_args = {} # to be passed into pydantic.create_model
        
        # Config to be passed into pydantic.create_model __configs__ param
        class Config:
            fields = {}
            schema_extra={
                'required':[] # Handling 'required' in schema extra
            }
                
        for field_name, field in s.get_fields().items():
            
            Config.fields[field_name] = {}
            
            # Handle case where field is a ListSerializer
            # e.g. my_field =  MySerializer(many=True)
            if isinstance(field, serializers.ListSerializer):
                
                t = List[cls.from_serializer(field.child)]
                
                if hasattr(field, 'max_length'):
                    Config.fields[field_name].update({'max_items':field.max_length})
                
                if hasattr(field, 'min_length'):
                    Config.fields[field_name].update({'min_items':field.min_length})
            
            # Handle ListField
            elif isinstance(field, fields.ListField):
            
                t = List[cls.infer_field_type(field.child)]
                
                if hasattr(field, 'max_length'):
                    Config.fields[field_name].update({'max_items':field.max_length})
                
                if hasattr(field, 'min_length'):
                    Config.fields[field_name].update({'min_items':field.min_length})
                    
            else:
                
                # Handle case where field is a normal serializer         
                if hasattr(field, 'get_fields'):
                    t = cls.from_serializer(field)
                else:
                    t = cls.infer_field_type(field)

            default = ...
            
            if field.default != fields.empty:
                default = field.default
                
            if field.required:    
                # DRF does not allow setting both `required` and `default`
                # So if field is required, pass ... as the default value
                create_model_args[field_name] = (t, ...)
                Config.schema_extra['required'].append(field_name)
            else:
                create_model_args[field_name] = (Optional[t], default)
                
            Config.fields[field_name].update(field_to_pydantic_args(field))
        
        model = create_model(name, **create_model_args, __config__=Config)
        model.__doc__ = s.__doc__
            
        return model

    def to_model(self):

        if isinstance(self.s, serializers.ListSerializer):
            return self.from_list_serializer(self.s)
        
        if isinstance(self.s, serializers.Serializer):
            return self.from_serializer(self.s)

        
        
