# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'File.ro_version'
        db.alter_column(u'files_file', 'ro_version', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'File.ro_version'
        raise RuntimeError("Cannot reverse this migration. 'File.ro_version' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'File.ro_version'
        db.alter_column(u'files_file', 'ro_version', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'developer.developer': {
            'Meta': {'object_name': 'Developer'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'avatar': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'avatar_thumb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'bio': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'denied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'developer_path': ('django.db.models.fields.CharField', [], {'max_length': '450'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'foldername': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'googleplus': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'referral': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'releases': ('django.db.models.fields.TextField', [], {}),
            'rootzwiki': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'services': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['developer.Developer']", 'null': 'True', 'blank': 'True'}),
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
            'ro_board': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ro_developerid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ro_rom': ('django.db.models.fields.CharField', [], {'max_length': '65', 'blank': 'True'}),
            'ro_version': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['files']