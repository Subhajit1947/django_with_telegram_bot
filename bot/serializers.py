from .models import Post
from rest_framework import serializers
class PostSerializer(serializers.ModelSerializer):  # Changed name to singular (convention)
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('owner', 'created_at')  # These should be read-only

    def create(self, validated_data):
        user = self.context["request"].user
        post = Post.objects.create(owner=user, **validated_data)  # Changed 'author' to 'owner'
        return post