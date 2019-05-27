from django.contrib.sessions.backends import file
from rest_framework.serializers import ModelSerializer

from files.models import File


class FileSerializer(ModelSerializer):

    class Meta:
        model = File
        files = ['file']
        fields = '__all__'