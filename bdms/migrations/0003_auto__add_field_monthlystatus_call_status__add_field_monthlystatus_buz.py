# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MonthlyStatus.call_status'
        db.add_column(u'bdms_monthlystatus', 'call_status',
                      self.gf('django.db.models.fields.CharField')(default='Answered', max_length=20),
                      keep_default=False)

        # Adding field 'MonthlyStatus.buzz_friend'
        db.add_column(u'bdms_monthlystatus', 'buzz_friend',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TrainingBatch.partner'
        db.add_column(u'bdms_trainingbatch', 'partner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['bdms.Partner']),
                      keep_default=False)

        # Adding field 'TrainingBatch.mobilization_date'
        db.add_column(u'bdms_trainingbatch', 'mobilization_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'TrainingBatch.training_date'
        db.add_column(u'bdms_trainingbatch', 'training_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'TrainingBatch.training_batch_size'
        db.add_column(u'bdms_trainingbatch', 'training_batch_size',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)

        # Deleting field 'Trainee.training_date'
        db.delete_column(u'bdms_trainee', 'training_date')

        # Deleting field 'Trainee.partner'
        db.delete_column(u'bdms_trainee', 'partner_id')

        # Deleting field 'Trainee.mobilization_date'
        db.delete_column(u'bdms_trainee', 'mobilization_date')


    def backwards(self, orm):
        # Deleting field 'MonthlyStatus.call_status'
        db.delete_column(u'bdms_monthlystatus', 'call_status')

        # Deleting field 'MonthlyStatus.buzz_friend'
        db.delete_column(u'bdms_monthlystatus', 'buzz_friend')

        # Deleting field 'TrainingBatch.partner'
        db.delete_column(u'bdms_trainingbatch', 'partner_id')

        # Deleting field 'TrainingBatch.mobilization_date'
        db.delete_column(u'bdms_trainingbatch', 'mobilization_date')

        # Deleting field 'TrainingBatch.training_date'
        db.delete_column(u'bdms_trainingbatch', 'training_date')

        # Deleting field 'TrainingBatch.training_batch_size'
        db.delete_column(u'bdms_trainingbatch', 'training_batch_size')

        # Adding field 'Trainee.training_date'
        db.add_column(u'bdms_trainee', 'training_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Trainee.partner'
        db.add_column(u'bdms_trainee', 'partner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['bdms.Partner']),
                      keep_default=False)

        # Adding field 'Trainee.mobilization_date'
        db.add_column(u'bdms_trainee', 'mobilization_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'bdms.basemodel': {
            'Meta': {'object_name': 'BaseModel'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'bdms_basemodel_created_set'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edited_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_edited_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'bdms_basemodel_edited_set'", 'to': u"orm['auth.User']"})
        },
        u'bdms.block': {
            'Meta': {'object_name': 'Block', '_ormbases': [u'bdms.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bdms.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bdms.District']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'bdms.district': {
            'Meta': {'object_name': 'District', '_ormbases': [u'bdms.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bdms.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bdms.State']"})
        },
        u'bdms.monthlystatus': {
            'Meta': {'object_name': 'MonthlyStatus', '_ormbases': [u'bdms.BaseModel']},
            'are_you_happier_than_before': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            'are_you_maintaining_accounts': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bdms.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'buzz_friend': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'call_status': ('django.db.models.fields.CharField', [], {'default': "'Answered'", 'max_length': '20'}),
            'difference_between_income_and_profit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'do_you_feel_confident_to_solve_your_challenges': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            'feedback_collected_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'feedback_collected_date': ('django.db.models.fields.DateField', [], {}),
            'from_where_did_you_take_a_new_loan': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'have_you_expanded_your_business': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            'have_you_started_a_new_business': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'have_you_taken_a_new_loan': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            'how_did_you_expanded_your_business': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'how_much_of_your_goals_have_you_reached': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'interested_in_joining_buzz_plus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            'post_training_income': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True'}),
            'post_training_profit': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True'}),
            'post_training_savings': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True'}),
            'trainee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bdms.Trainee']"})
        },
        u'bdms.partner': {
            'Meta': {'object_name': 'Partner', '_ormbases': [u'bdms.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bdms.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bdms.place': {
            'Meta': {'object_name': 'Place', '_ormbases': [u'bdms.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bdms.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bdms.Block']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'bdms.state': {
            'Meta': {'object_name': 'State', '_ormbases': [u'bdms.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bdms.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'bdms.trainee': {
            'Meta': {'object_name': 'Trainee', '_ormbases': [u'bdms.BaseModel']},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bdms.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'business': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_mobile': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'current_challenges': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'current_monthly_income': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'current_monthly_profit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'current_monthly_savings': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'literacy_level': ('django.db.models.fields.CharField', [], {'default': "'Illiterate'", 'max_length': '20', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bdms.Place']"}),
            'training_batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bdms.TrainingBatch']"})
        },
        u'bdms.trainingbatch': {
            'Meta': {'object_name': 'TrainingBatch', '_ormbases': [u'bdms.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bdms.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'mobilization_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bdms.Partner']"}),
            'training_batch_size': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'training_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bdms']