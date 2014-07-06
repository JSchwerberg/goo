import time
import hashlib
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import File
from developer.models import Developer
from .helpers import get_next_folders

SECRET_KEY = "93heq298unrf312890h"

def file_download(request):
    
    path = request.session['file']
    if path[:5] == '/devs':
        path = path[5:]

    if ('sponsor' in request.session) or ('waited' in request.session and request.session['waited'] < int(time.time())):
        expire = int(time.time()) + 2400
        token = hashlib.md5("%s?ttl=%s&pass=%s" % (path, expire, SECRET_KEY))
        token = token.hexdigest()
        try:
            del request.session['waited']
        except KeyError:
            pass
        return redirect('http://cdn.goo.im%s?ttl=%s&token=%s' % (path,expire,token))

    request.session['waited'] = int(time.time()) + 10        
    return render(request, "files/file_download.html", {"path": path})


def file_list(request, cur_path=''):

    # Normalize to Database structure with leading '/'
    cur_path = '/devs/' + cur_path

    # Strip Trailing slash if it's there
    if cur_path[-1] == '/':
		cur_path = cur_path[:-1]


    if cur_path == '/devs':
        folder_qs = Developer.objects.order_by('developer_path')
        paginator = Paginator(folder_qs, 50)
        page = request.GET.get('page')

        try:
            folders = paginator.page(page)
        except PageNotAnInteger:
            folders = paginator.page(1)
        except EmptyPage:
            folders = paginator.page(paginator.num_pages)

        folder_list = []
        for obj in folders:
            folder_list.append(obj.developer_path[6:])
        breadcrumbs = [['devs', '/devs']]
        return render(request, 'files/file_list.html', {"folders": sorted(folder_list), "breadcrumbs": breadcrumbs})

    try:
        query = File.objects.get(path=cur_path)
    except:
        pass
    else:
        request.session['file'] = query.path
        return file_download(request)
		
    # List of all the files in the folder
    qs = File.objects.filter(folder=cur_path).order_by('filename')
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
    request.session['file'] = '/gapps/' + path
    return file_download(request)
