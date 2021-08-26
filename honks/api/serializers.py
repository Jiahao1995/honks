from rest_framework import serializers

from accounts.api.serializers import UserSerializer
from honks.models import Honk


class HonkSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Honk
        fields = ('id', 'user', 'created_at', 'content')


class HonkCreateSerializer(serializers.ModelSerializer):
    content = serializers.CharField(min_length=6, max_length=140)

    class Meta:
        model = Honk
        fields = ('content',)

    def create(self, validated_data):
        user = self.context['request'].user
        content = validated_data['content']
        honk = Honk.objects.create(user=user, content=content)
        return honk