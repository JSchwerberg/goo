# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Sponsor.user'
        db.delete_column(u'sponsor_sponsor', 'user_id')

        # Adding field 'Sponsor.username'
        db.add_column(u'sponsor_sponsor', 'username',
                      self.gf('django.db.models.fields.CharField')(default='deaduser', max_length=100),
                      keep_default=False)

        # Adding field 'Sponsor.password'
        db.add_column(u'sponsor_sponsor', 'password',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64),
                      keep_default=False)

        # Adding field 'Sponsor.created'
        db.add_column(u'sponsor_sponsor', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 7, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Sponsor.status'
        db.add_column(u'sponsor_sponsor', 'status',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Sponsor.salt'
        db.add_column(u'sponsor_sponsor', 'salt',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64),
                      keep_default=False)

        # Adding field 'Sponsor.email'
        db.add_column(u'sponsor_sponsor', 'email',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Sponsor.migrated'
        db.add_column(u'sponsor_sponsor', 'migrated',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Sponsor.user'
        raise RuntimeError("Cannot reverse this migration. 'Sponsor.user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Sponsor.user'
        db.add_column(u'sponsor_sponsor', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Deleting field 'Sponsor.username'
        db.delete_column(u'sponsor_sponsor', 'username')

        # Deleting field 'Sponsor.password'
        db.delete_column(u'sponsor_sponsor', 'password')

        # Deleting field 'Sponsor.created'
        db.delete_column(u'sponsor_sponsor', 'created')

        # Deleting field 'Sponsor.status'
        db.delete_column(u'sponsor_sponsor', 'status')

        # Deleting field 'Sponsor.salt'
        db.delete_column(u'sponsor_sponsor', 'salt')

        # Deleting field 'Sponsor.email'
        db.delete_column(u'sponsor_sponsor', 'email')

        # Deleting field 'Sponsor.migrated'
        db.delete_column(u'sponsor_sponsor', 'migrated')


    models = {
        u'sponsor.authkey': {
            'Meta': {'object_name': 'AuthKey'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'sponsor.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'migrated': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'payment_id': ('django.db.models.fields.CharField', [], {'default': "'DEVELOPER'", 'max_length': '32'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['sponsor']