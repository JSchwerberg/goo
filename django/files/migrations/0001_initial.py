# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SearchIndex'
        db.create_table(u'files_searchindex', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('folder', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=8)),
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
        ))
        db.send_create_signal(u'files', ['SearchIndex'])


    def backwards(self, orm):
        # Deleting model 'SearchIndex'
        db.delete_table(u'files_searchindex')


    models = {
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