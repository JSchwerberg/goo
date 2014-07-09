# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InstallCommand'
        db.create_table(u'recovery_installcommand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('command', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'recovery', ['InstallCommand'])


    def backwards(self, orm):
        # Deleting model 'InstallCommand'
        db.delete_table(u'recovery_installcommand')


    models = {
        u'recovery.installcommand': {
            'Meta': {'object_name': 'InstallCommand'},
            'command': ('django.db.models.fields.TextField', [], {}),
            'device': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['recovery']