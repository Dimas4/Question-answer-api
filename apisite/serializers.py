from rest_framework.serializers import ModelSerializer
from glavapp.models import Message


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'user',
            'message',
            'data_new'
        ]
