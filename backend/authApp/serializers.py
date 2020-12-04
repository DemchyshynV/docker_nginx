from rest_framework.serializers import ModelSerializer

from .models import InviteModel


class InviteSerializer(ModelSerializer):
    class Meta:
        model = InviteModel
        fields = '__all__'
        read_only_fields = ['uuid']
        extra_kwargs = {'isMentor': {'write_only': True}}
