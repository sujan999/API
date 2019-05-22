from rest_framework import serializers
from home.models import Post
# converts to JSON
# validation


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'date',
        ]
        read_only_fields = ['id']

        def validate_title(self, value):
            qs = Post.objects.filter(title__iexact=value)
            if self .instance:
                qs = qs.exclude(id=self.instance.id)
            if qs.exists():
                raise serializers.valaidationError('This title already exist')
            return value
