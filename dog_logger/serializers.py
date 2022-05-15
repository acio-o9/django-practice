from .models import Owner

from rest_framework import serializers


class OwnerSerializer(serializers.ModelSerializer):
    name_with_suffix = serializers.SerializerMethodField()
    class Meta:
        model = Owner
        fields = ['id', 'name', 'name_with_suffix']

    def get_name_with_suffix(self, owner):
        return f'{owner.name} san'

