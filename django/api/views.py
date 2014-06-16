#from django.shortcuts import render
#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.pagination import Paginator, EmptyPage, PageNotAnInteger
from files.models import File
from files.serializers import PaginatedFileSerializer


@api_view('GET')
def file_list(request):
    """
    List all files in the file index, paginated.  Supports an optional 
    'search' query parameter, that filters the results by the search terms,
    an optional 'items' parameter that allows the end-user to specify
    how many items per page, and a 'page' parameter to get a specific
    page number from the results.
    """

    # We only want to show items that are 'active'
    queryset = File.objects.all().filter(status=1)

    # Set optional search terms
    search_terms = request.QUERY_PARAMS.get('search')
    if search_terms not None:
    	# Equivalent to "SELECT * from files WHERE MATCH(files, filename)  
    	# AGAINST (search_terms IN BOOLEAN MODE) OR MATCH(files, description) 
    	# AGAINST (search_terms IN BOOLEAN MODE)"
    	queryset = queryset.filter(Q(filename__search=search_terms) | 
    		Q(description__search=search_terms))

    # Sort queryset by modified date (descending),  
    # removing any duplicate entries
    queryset = queryset.order_by('-modified').distinct('id')
    
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
