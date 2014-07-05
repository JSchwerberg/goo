import time
import hashlib
from django.shortcuts import render
from .models import File
from .helpers import get_next_folders


def file_download(request, query):
	path = query.path
	expire = time.gmtime() + 2400
	token = hashlib.md5("%s?ttl=%s&pass=%s" % (path, expire, SECRET_KEY))

	return render(request, 'files/file_download.html', {"path": query.path, "filename": query.filename, "expire": expire, "token": token} )


def file_list(request, cur_path):

	if cur_path[-1] == '/':
		cur_path = cur_path[:-1]

	try:
		query = File.objects.get(path=cur_path)
	except:
		continue
	else:
		return file_download(request, query)
		

	qs = File.objects.filter(folder=cur_path)
	folder_qs = File.objects.filter(folder__startswith=cur_path + '/')

	folder_list = []
	for obj in folder_qs:
		folder_list.append(obj.folder)

	# Returns a list of folder names, one
    # level deeper than the current path 

	folders = get_next_folders(cur_path, folder_list) 

	return render(request, 'files/file_list.html', {"folders": folders, "files": qs})


