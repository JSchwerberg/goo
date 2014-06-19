from django.db import models

# Create your models here.

class File(models.Model):
    filename = models.CharField(max_length=250)
    path = models.CharField(max_length=350)
    folder = models.CharField(max_length=350)
    md5 = models.CharField(max_length=32)
    filetype = models.CharField(max_length=8)
    description = models.TextField()
    is_flashable = models.BooleanField(default=False)
    modified = models.CharField(max_length=35)
    status = models.SmallIntegerField(default=1)
    additional_info = models.TextField()
    short_url = models.CharField(max_length=32)
    developer_id = models.IntegerField(default=5)
    ro_developerid = models.CharField(max_length=50)
    ro_board = models.CharField(max_length=50)
    ro_rom = models.CharField(max_length=65)
    ro_version = models.IntegerField()
    gapps_package = models.IntegerField()
    incremental_file = models.IntegerField()
    filesize = models.BigIntegerField()
    download_count = models.PositiveIntegerField(default=0)
    last_download = models.DateTimeField(auto_now=True)

class Blacklist(models.Model):
    keyword = models.CharField(max_length=150)
    status = models.BooleanField()

