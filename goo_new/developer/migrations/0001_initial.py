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
            ('password', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('avatar', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('avatar_thumb', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('rootzwiki', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('xda', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('googleplus', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('xda_rd_url', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')()),
            ('denied', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'developer', ['Developer'])

        # Adding model 'Application'
        db.create_table(u'developer_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('googleplus', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('xda', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('releases', self.gf('django.db.models.fields.TextField')()),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('foldername', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('services', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('referral', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('processed', self.gf('django.db.models.fields.BooleanField')()),
            ('denied', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'developer', ['Application'])


    def backwards(self, orm):
        # Deleting model 'Developer'
        db.delete_table(u'developer_developer')

        # Deleting model 'Application'
        db.delete_table(u'developer_application')


    models = {
        u'developer.application': {
            'Meta': {'object_name': 'Application'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'bio': ('django.db.models.fields.TextField', [], {}),
            'denied': ('django.db.models.fields.BooleanField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'foldername': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'googleplus': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processed': ('django.db.models.fields.BooleanField', [], {}),
            'referral': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'releases': ('django.db.models.fields.TextField', [], {}),
            'services': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'xda': ('django.db.models.fields.CharField', [], {'max_length': '350'})
        },
        u'developer.developer': {
            'Meta': {'object_name': 'Developer'},
            'avatar': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'avatar_thumb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'bio': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'denied': ('django.db.models.fields.BooleanField', [], {}),
            'developer_path': ('django.db.models.fields.CharField', [], {'max_length': '450'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'googleplus': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rootzwiki': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'status': ('django.db.models.fields.BooleanField', [], {}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'xda': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'xda_rd_url': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['developer']