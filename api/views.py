#from django.shortcuts import render
#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from files.models import SearchIndex
from files.serializers import IndexSerializer


@api_view(['GET','POST'])
def file_list(request):
    """
    List all files, or create a new file
    """
    if request.method == 'GET':
        files = SearchIndex.objects.all()
        serializer = IndexSerializer(files, many=True)
