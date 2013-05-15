# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feed'
        db.create_table(u'reader_feed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=255)),
        ))
        db.send_create_signal(u'reader', ['Feed'])

        # Adding model 'NewsLine'
        db.create_table(u'reader_newsline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reader.Feed'])),
            ('published', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('link_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'reader', ['NewsLine'])

        # Adding unique constraint on 'NewsLine', fields ['feed', 'link_id']
        db.create_unique(u'reader_newsline', ['feed_id', 'link_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'NewsLine', fields ['feed', 'link_id']
        db.delete_unique(u'reader_newsline', ['feed_id', 'link_id'])

        # Deleting model 'Feed'
        db.delete_table(u'reader_feed')

        # Deleting model 'NewsLine'
        db.delete_table(u'reader_newsline')


    models = {
        u'reader.feed': {
            'Meta': {'object_name': 'Feed'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'reader.newsline': {
            'Meta': {'unique_together': "(('feed', 'link_id'),)", 'object_name': 'NewsLine'},
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reader.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['reader']