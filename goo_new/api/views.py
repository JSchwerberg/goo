import base64
import simplejson as json
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from files.models import File
from developer.models import Developer
from files.models import File
from recovery.models import InstallCommand
from .serializers import PaginatedFileSerializer, FileSerializer, DeveloperSerializer
from .serializers import DevFileSerializer, GappsSerializer, InstallCommandSerializer
from .authentication import TokenAuthentication


@api_view(['GET', 'POST'])
def file_list(request, folder=None):
    """
    List all files in the file index, paginated.  Supports an optional 
    'search' query parameter, that filters the results by the search terms,
    an optional 'items' parameter that allows the end-user to specify
    how many items per page, and a 'page' parameter to get a specific
    page number from the results.
    """

    if request.method == 'GET':
        # We only want to show items that are 'active'
        if folder == None:
            queryset = File.objects.all().filter(status=1)
        else:
            if folder[-1] == '/':
                folder = folder[:-1]
            try:
                queryset = File.objects.all().filter(status=1, folder='/' + folder)
            except:
                return file_detail(request, path=folder)

        # Set optional search terms
        search_terms = request.QUERY_PARAMS.get('search')
        if search_terms:
        	# Equivalent to "SELECT * from files WHERE MATCH(files, filename)  
        	# AGAINST (search_terms IN BOOLEAN MODE) OR MATCH(files, description) 
        	# AGAINST (search_terms IN BOOLEAN MODE)"
        	queryset = queryset.filter(Q(filename__search=search_terms) | 
        		Q(description__search=search_terms))

        # Sort queryset by modified date (descending),  
        # removing any duplicate entries
        queryset = queryset.order_by('-modified').distinct()
        
        # Allow API end-users to specify a custom amount of items per page
        items_per_page = request.QUERY_PARAMS.get('items') 
        if not items_per_page or not isinstance(items_per_page, int):
        	items_per_page = 10

    	paginator = Paginator(queryset, items_per_page)
        
        page = request.QUERY_PARAMS.get('page')
        try:
        	files = paginator.page(page)
        except PageNotAnInteger:
        	# If page is not an integer, deliver first page
        	files = paginator.page(1)
        except EmptyPage:
        	# If page is out of range
        	# deliver last page of results
        	files = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = PaginatedFileSerializer(files, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = FileSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def file_detail(request, pk=None, path=None):
    """
    Retrieve, update, or delete a specific file
    """

    if (pk != None):
        try:
            file = File.objects.get(pk=pk)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif (path != None):
        try:
            file = File.objects.get(path=path)
        except File.DoesNotExist:  
            try:
                file = File.objects.get(path='/devs/' + path)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = FileSerializer(file)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FileSerializer(file, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Repsonse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def developer_file_list(request, dev):
    """
    List files by a given developer
    """

    if request.method == 'GET':
        if dev[-1] = '/':
            dev = dev[:-1]

        # We only want to show items that are 'active'
        queryset = File.objects.filter(developer__developer_path='/devs/' + dev).order_by('-modified')
        
        # Allow API end-users to specify a custom amount of items per page
        items_per_page = request.QUERY_PARAMS.get('items') 
        if not items_per_page or not isinstance(items_per_page, int):
            items_per_page = 10

        paginator = Paginator(queryset, items_per_page)
        
        page = request.QUERY_PARAMS.get('page')
        try:
            files = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page
            files = paginator.page(1)
        except EmptyPage:
            # If page is out of range
            # deliver last page of results
            files = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = PaginatedFileSerializer(files, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def developer_info(request, path):
    if request.method == 'GET':
        queryset = Developer.objects.filter(developer_path__exact='/devs/%s' % path)
        serializer = DeveloperSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        post_body = request.body
        post_data = json.loads(post_body)
        encoded_data = post_data['Data']
        print encoded_data
        decoded_data = base64.b64decode(encoded_data)
        data = json.loads(decoded_data)
        try:
            duplicate = File.objects.get(path='%s' % data['path'])
        except:
            serializer = FileSerializer(data=data)
        else:
            serializer = FileSerializer(duplicate, data=data)
            if serializer.is_valid():
                serializer.save()
        split_path = path.split('/')
        if 'devs' in split_path:
            split_path.remove('devs')

        devfolder = split_path[0]

        try:
            developer = Developer.objects.get(developer_path='/devs/%s' % devfolder)
        except:
            split_string = path.split('/')
            username = split_string[0]
            developer = Developer.objects.get(username=devfolder)

        if serializer.is_valid():
            serializer.object.developer = developer
            if serializer.object.ro_developerid == "":
                serializer.object.ro_developerid = serializer.object.developer.username
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def latest_ics(request):
    if request.method == 'GET':
        query = Files.objects.filter(ro_developerid='gapps', 
                ro_rom='ICS').order_by('-ro_version')[0:1]
        serializer = GappsSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def latest_jb(request):
    if request.method == 'GET':
        query = Files.objects.filter(ro_developerid='gapps', 
                ro_rom='JB').order_by('-ro_version')[0:1]
        serializer = GappsSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def install_command_view(request, device):
    if request.method == 'GET':
        try:
            query = InstallCommand.objects.get(device=device)
        except InstallCommand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InstallCommandSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)        
