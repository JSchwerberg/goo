# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'File.developer_id' to match new field type.
        db.rename_column(u'files_file', 'developer_id', 'developer_id_id')
        # Changing field 'File.developer_id'
        db.alter_column(u'files_file', 'developer_id_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['developer.Developer']))
        # Adding index on 'File', fields ['developer_id']
        db.create_index(u'files_file', ['developer_id_id'])


        # Changing field 'File.incremental_file'
        db.alter_column(u'files_file', 'incremental_file', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Removing index on 'File', fields ['developer_id']
        db.delete_index(u'files_file', ['developer_id_id'])


        # Renaming column for 'File.developer_id' to match new field type.
        db.rename_column(u'files_file', 'developer_id_id', 'developer_id')
        # Changing field 'File.developer_id'
        db.alter_column(u'files_file', 'developer_id', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'File.incremental_file'
        db.alter_column(u'files_file', 'incremental_file', self.gf('django.db.models.fields.IntegerField')(default=''))

    models = {
        u'developer.application': {
            'Meta': {'object_name': 'Application'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'denied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'foldername': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'referral': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'releases': ('django.db.models.fields.TextField', [], {}),
            'services': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'developer.developer': {
            'Meta': {'object_name': 'Developer'},
            'application': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['developer.Application']", 'unique': 'True'}),
            'avatar': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'avatar_thumb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'bio': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'developer_path': ('django.db.models.fields.CharField', [], {'max_length': '450'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'foldername': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'googleplus': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rootzwiki': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'xda': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'xda_rd_url': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'files.blacklistkeyword': {
            'Meta': {'object_name': 'BlacklistKeyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'status': ('django.db.models.fields.BooleanField', [], {})
        },
        u'files.file': {
            'Meta': {'object_name': 'File'},
            'additional_info': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'developer_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['developer.Developer']"}),
            'download_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'filesize': ('django.db.models.fields.BigIntegerField', [], {}),
            'filetype': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'gapps_package': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incremental_file': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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