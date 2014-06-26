# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Developer'
        db.create_table(u'developer_developer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('developer_path', self.gf('django.db.models.fields.CharField')(max_length=450)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('avatar', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('avatar_thumb', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('releases', self.gf('django.db.models.fields.TextField')()),
            ('services', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('referral', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('processed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('denied', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('foldername', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('rootzwiki', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('xda', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('googleplus', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('xda_rd_url', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'developer', ['Developer'])


    def backwards(self, orm):
        # Deleting model 'Developer'
        db.delete_table(u'developer_developer')


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
            'foldername': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
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
        }
    }

    complete_apps = ['developer']