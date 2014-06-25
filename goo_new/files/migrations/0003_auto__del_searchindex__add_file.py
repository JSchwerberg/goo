# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SearchIndex'
        db.delete_table(u'files_searchindex')

        # Adding model 'File'
        db.create_table(u'files_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('folder', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('filetype', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('is_flashable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('modified', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('downloads', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('additional_info', self.gf('django.db.models.fields.TextField')()),
            ('short_url', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('developer_id', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('ro_developerid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ro_board', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ro_rom', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('ro_version', self.gf('django.db.models.fields.IntegerField')()),
            ('gapps_package', self.gf('django.db.models.fields.IntegerField')()),
            ('incremental_file', self.gf('django.db.models.fields.IntegerField')()),
            ('filesize', self.gf('django.db.models.fields.BigIntegerField')()),
            ('download_count', self.gf('django.db.models.fields.BigIntegerField')()),
            ('last_download', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'files', ['File'])


    def backwards(self, orm):
        # Adding model 'SearchIndex'
        db.create_table(u'files_searchindex', (
            ('short_url', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('gapps_package', self.gf('django.db.models.fields.IntegerField')()),
            ('developer_id', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('ro_board', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ro_version', self.gf('django.db.models.fields.IntegerField')()),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('incremental_file', self.gf('django.db.models.fields.IntegerField')()),
            ('filesize', self.gf('django.db.models.fields.BigIntegerField')()),
            ('folder', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('ro_rom', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('downloads', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('additional_info', self.gf('django.db.models.fields.TextField')()),
            ('ro_developerid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('modified', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('is_flashable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'files', ['SearchIndex'])

        # Deleting model 'File'
        db.delete_table(u'files_file')


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
            'download_count': ('django.db.models.fields.BigIntegerField', [], {}),
            'downloads': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'filesize': ('django.db.models.fields.BigIntegerField', [], {}),
            'filetype': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'gapps_package': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incremental_file': ('django.db.models.fields.IntegerField', [], {}),
            'is_flashable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_download': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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