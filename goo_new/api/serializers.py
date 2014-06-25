from django.forms import widgets
from rest_framework.pagination import PaginationSerializer
from rest_framework import serializers
from .files.models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        
        # Only these fields should be exposed by the API /at all/
        fields = ('id', 'filename', 'path', 'folder', 'md5', 'filetype', 'description', 
        	'is_flashable', 'modified', 'ro_developerid', 'ro_board',  
        	'ro_rom', 'ro_version', 'gapps_package' 'filesize', 
        	'download_count', 'last_download' )

        # Don't show 'filename' or 'folder' in the results -- path will combine these
        write_only_fields = {'filename', 'folder'}

        # API should not be modifying download_count or last_download
        read_only_fields = {'download_count', 'last_download'}


class PaginatedFileSerializer(PaginationSerializer):
	class Meta:
		object_serializer_class = FileSerializer