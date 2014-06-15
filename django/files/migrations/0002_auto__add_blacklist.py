# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blacklist'
        db.create_table(u'files_blacklist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('status', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'files', ['Blacklist'])


    def backwards(self, orm):
        # Deleting model 'Blacklist'
        db.delete_table(u'files_blacklist')


    models = {
        u'files.blacklist': {
            'Meta': {'object_name': 'Blacklist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'status': ('django.db.models.fields.BooleanField', [], {})
        },
        u'files.searchindex': {
            'Meta': {'object_name': 'SearchIndex'},
            'additional_info': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'developer_id': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'downloads': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'filesize': ('django.db.models.fields.BigIntegerField', [], {}),
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'gapps_package': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incremental_file': ('django.db.models.fields.IntegerField', [], {}),
            'is_flashable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'modified': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'ro_board': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ro_developerid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ro_rom': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'ro_version': ('django.db.models.fields.IntegerField', [], {}),
            'short_url': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['files']