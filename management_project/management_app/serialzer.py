from rest_framework import serializers
from django.core.files.base import ContentFile
import base64
import uuid
from .models import *

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'{uuid.uuid4()}.{ext}')
        return super().to_internal_value(data)

class StudentProfileSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = StudentProfile
        fields = ('first_name','last_name','email','date_of_birth','image','student_class')