from rest_framework import serializers

class ArticleUpdateSerializer(serializers.Serializer):
    pk = serializers.IntegerField(help_text="Primary key of article to update")
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    
class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(required=True, help_text="Name of category")
    