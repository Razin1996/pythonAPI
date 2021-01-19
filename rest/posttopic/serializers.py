from rest_framework import serializers
from .models import send_command

class send_commandSerializers(serializers.ModelSerializer):
    class Meta:
        model = send_command
        fields = "__all__"