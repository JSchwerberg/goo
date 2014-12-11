import time
import hashlib
import re
import simplejson as json
from datetime import datetime
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from .models import File, BlacklistKeyword
from developer.models import Developer
from .helpers import get_next_folders

SECRET_KEY = settings.GAPPS_KEY

def file_download(request):
    
    file_obj = request.session['file']
    path = file_obj.path
    if path[:5] == '/devs':
        path = path[5:]

    download_page = True
    try:
        viewed = request.session['list_viewed']
    except:
        viewed = False
        try: 
            if request.session['download_page'] == True:
                download_page = True
        except:
            download_page = False
            pass
    
    cur_time = int(time.time())


    if download_page == True:
#    if ('sponsor' in request.session) or ('waited' in request.session and request.session['waited'] < int(time.time())):
        expire = int(time.time()) + 2400
        token = hashlib.md5("%s?ttl=%s&pass=%s" % (path, expire, SECRET_KEY))
        token = token.hexdigest()
        try:
            del request.session['waited']
        except KeyError:
            pass
        try:
            del request.session['list_viewed']
        except KeyError:
            pass
        try:
            del request.session['download_page']
        except KeyError:
            pass
        
        file_obj.download_count += 1
        file_obj.last_download = datetime.now()
        file_obj.save() 
        return redirect('http://cdn.goo.im%s?ttl=%s&token=%s' % (path,expire,token))

    else:
        request.session['download_page'] = True
        return render(request, 'files/download.html', {"file": file_obj})

#    request.session['waited'] = int(time.time()) + 10        
#    return render(request, "files/file_download.html", {"path": path})


@csrf_exempt
def file_list(request, cur_path=''):

    if request.method == 'POST':
        post_data = request.body
        json_data = json.loads(post_data)
        user = json_data['user']
        token = json_data['token']
        if cache.get('apitoken_%s' % user) == token and token != None:
            request.session['sponsor'] = user

    
    qd = request.GET
    if 'user' in qd and 'token' in qd:
        user = qd['user']
        token = qd['token']
        if cache.get('apitoken_%s' % user) == token and token != None:
            request.session['sponsor'] = user

    # Normalize to Database structure with leading '/'
    cur_path = '/devs/' + cur_path

    # Strip Trailing slash if it's there
    if cur_path[-1] == '/':
		cur_path = cur_path[:-1]


    if cur_path == '/devs':
        folder_qs = Developer.objects.order_by('developer_path')
        page = request.GET.get('page')

        folder_list = []
        for obj in folder_qs:
            folder_list.append(obj.developer_path[6:])

        folder_list = sorted(folder_list, cmp=lambda x,y: cmp(x.lower(), y.lower()))

        paginator = Paginator(folder_list, 50)
        
        try:
            folders = paginator.page(page)
        except PageNotAnInteger:
            folders = paginator.page(1)
        except EmptyPage:
            folders = paginator.page(paginator.num_pages)
        breadcrumbs = [['devs', '/devs']]
        request.session['list_viewed'] = int(time.time()) + 300
        return render(request, 'files/file_list.html', {"folders": folders, "breadcrumbs": breadcrumbs})

    try:
        query = File.objects.get(path=cur_path)
    except:
        pass
    else:
        request.session['file'] = query
        return file_download(request)
		
    # List of all the files in the folder

    blacklist = BlacklistKeyword.objects.filter(status=1)

    exclude = []
    for word in blacklist:
        inner_qs = File.objects.filter(path__icontains=word.keyword)
        for result in inner_qs:
            exclude.append(result.id)

    
    qs = File.objects.filter(folder=cur_path).exclude(id__in=exclude).extra(select={'lower_file': 'lower(filename)'}).order_by('lower_file')


    paginator = Paginator(qs, 50)

    page = request.GET.get('page')

    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)
	
    # List of all the files in subfolders
    folder_qs = File.objects.filter(folder__startswith=cur_path + '/')

    folder_list = []
    for obj in folder_qs:
        if obj.folder not in folder_list:
            folder_list.append(obj.folder)

    bc_path = cur_path[1:].split('/')
    breadcrumbs = []

    for item in bc_path:
        i = bc_path.index(item)
        url = ''
        for num in range(0, i + 1):
            url += '/%s' % bc_path[num]
        breadcrumbs.append([item, url])
        

	# Returns a list of folder names, one
    # level deeper than the current path 

    folders = get_next_folders(cur_path, folder_list) 

    return render(request, 'files/file_list.html', {"folders": folders, "files": files, "breadcrumbs": breadcrumbs})


def gapps_list(request):
    qs = File.objects.filter(folder='/devs/gapps')
    paginator = Paginator(qs, 50)

    page = request.GET.get('page')

    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)
    
    breadcrumbs = [['gapps', '/gapps']]

    return render(request, 'files/file_list.html', {"files": files, "breadcrumbs": breadcrumbs})

def gapps_download(request, path):
    request.session['file'] = File.objects.get(path='/devs/gapps/' + path)
    return file_download(request)

def file_search_result_list(request):

    search = request.GET.get('search')

    if len(search) == 32:
        try:
            files = File.objects.filter(md5=search)
        except:
            pass
        else:
            return render(request, 'files/search/results.html', {"files": files})

    try: 
        files = File.objects.filter(filename__contains=search)
    except:
        return render(request, 'files/search/results.html', {"files": None})
    
    return render(request, 'files/search/results.html', {"files": files})
