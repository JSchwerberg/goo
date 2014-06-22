# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'File.downloads'
        db.delete_column(u'files_file', 'downloads')


        # Changing field 'File.download_count'
        db.alter_column(u'files_file', 'download_count', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'File.last_download'
        db.alter_column(u'files_file', 'last_download', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    def backwards(self, orm):
        # Adding field 'File.downloads'
        db.add_column(u'files_file', 'downloads',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


        # Changing field 'File.download_count'
        db.alter_column(u'files_file', 'download_count', self.gf('django.db.models.fields.BigIntegerField')())

        # Changing field 'File.last_download'
        db.alter_column(u'files_file', 'last_download', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        u'files.blacklist': {
            'Meta': {'object_name': 'Blacklist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'status': ('django.db.models.fields.BooleanField', [], {})
        },
        u'files.file': {
            'Meta': {'object_name': 'File'},
            'additional_info': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'developer_id': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'download_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'filesize': ('django.db.models.fields.BigIntegerField', [], {}),
            'filetype': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'gapps_package': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incremental_file': ('django.db.models.fields.IntegerField', [], {}),
            'is_flashable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_download': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'modified': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'ro_board': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ro_developerid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ro_rom': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'ro_version': ('django.db.models.fields.IntegerField', [], {}),
            'short_url': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['files']