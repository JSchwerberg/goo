from django.forms import widgets
from rest_framework.pagination import PaginationSerializer
from rest_framework import serializers
from .files.models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'path', 'md5', 'filetype', 'description', 
        	'is_flashable', 'modified', 'downloads', 'ro_developerid', 
        	'ro_board', 'ro_rom', 'ro_version', 'filesize', 
        	'download_count', 'last_download' )

class PaginatedFileSerializer(PaginationSerializer):
	class Meta:
		object_serializer_class = FileSerializer