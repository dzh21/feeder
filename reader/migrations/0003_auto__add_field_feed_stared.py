# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Feed.stared'
        db.add_column(u'reader_feed', 'stared',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Feed.stared'
        db.delete_column(u'reader_feed', 'stared')


    models = {
        u'reader.feed': {
            'Meta': {'object_name': 'Feed'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'stared': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'reader.newsline': {
            'Meta': {'unique_together': "(('feed', 'link_id'),)", 'object_name': 'NewsLine'},
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reader.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'readed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['reader']