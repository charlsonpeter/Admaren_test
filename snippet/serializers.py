from rest_framework import serializers
from .models import *


# Register serializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', 'url')

# User serializer
class SnippetSerializer(serializers.ModelSerializer):
    tag_title = serializers.CharField(source='tag.title')
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Snippet
        fields = ('tag_title', 'content','username', 'date_created')

    def create(self, validated_data):
        tag = Tag.create(validated_data['tag']['title'])
        snippet = Snippet.objects.create(tag=tag, content=validated_data['content'], user=self.context['request'].user)
        return snippet

    def update(self, instance, validated_data):
        tag = Tag.create(validated_data['tag']['title'])
        instance.update(tag=tag, content=validated_data['content'])
        return instance[0]

class SnipeetLinkSerializer(serializers.HyperlinkedModelSerializer):
    tag_title = serializers.CharField(source='tag.title')
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Snippet
        fields = ('tag_title', 'content','username', 'date_created', 'url')
    def create(self, validated_data):
        tag = Tag.create(validated_data['tag']['title'])
        snippet = Snippet.objects.create(tag=tag, content=validated_data['content'], user=self.context['request'].user)
        return snippet

    def update(self, instance, validated_data):
        tag = Tag.create(validated_data['tag']['title'])
        instance.tag=tag
        instance.content=validated_data['content']
        instance.save()
        return instance
