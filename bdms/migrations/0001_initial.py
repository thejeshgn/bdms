# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BaseModel'
        db.create_table(u'bdms_basemodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'bdms_basemodel_created_set', to=orm['auth.User'])),
            ('last_edited_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'bdms_basemodel_edited_set', to=orm['auth.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_edited_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'bdms', ['BaseModel'])

        # Adding model 'State'
        db.create_table(u'bdms_state', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bdms.BaseModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'bdms', ['State'])

        # Adding model 'District'
        db.create_table(u'bdms_district', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bdms.BaseModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bdms.State'])),
        ))
        db.send_create_signal(u'bdms', ['District'])

        # Adding model 'Block'
        db.create_table(u'bdms_block', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bdms.BaseModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bdms.District'])),
        ))
        db.send_create_signal(u'bdms', ['Block'])

        # Adding model 'Place'
        db.create_table(u'bdms_place', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bdms.BaseModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bdms.Block'])),
        ))
        db.send_create_signal(u'bdms', ['Place'])

        # Adding model 'Partner'
        db.create_table(u'bdms_partner', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bdms.BaseModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bdms', ['Partner'])

        # Adding model 'TrainingBatch'
        db.create_table(u'bdms_trainingbatch', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bdms.BaseModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'bdms', ['TrainingBatch'])

        # Adding model 'Trainee'
        db.create_table(u'bdms_trainee', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bdms.BaseModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=20)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bdms.Place'])),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bdms.Partner'])),
            ('mobilization_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True)),
            ('training_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True)),
            ('training_batch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bdms.TrainingBatch'])),
            ('literacy_level', self.gf('django.db.models.fields.CharField')(default='Illiterate', max_length=20, null=True)),
            ('business', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('contact_mobile', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('current_monthly_income', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('current_monthly_profit', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('current_monthly_savings', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('current_challenges', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'bdms', ['Trainee'])

        # Adding model 'MonthlyStatus'
        db.create_table(u'bdms_monthlystatus', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bdms.BaseModel'], unique=True, primary_key=True)),
            ('trainee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bdms.Trainee'])),
            ('feedback_collected_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('feedback_collected_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('post_training_income', self.gf('django.db.models.fields.IntegerField')()),
            ('post_training_profit', self.gf('django.db.models.fields.IntegerField')()),
            ('post_training_savings', self.gf('django.db.models.fields.IntegerField')()),
            ('difference_between_income_and_profit', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('are_you_maintaining_accounts', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('how_much_of_your_goals_have_you_reached', self.gf('django.db.models.fields.TextField')()),
            ('have_you_started_a_new_business', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('have_you_expanded_your_business', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('how_did_you_expanded_your_business', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('have_you_taken_a_new_loan', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('from_where_did_you_take_a_new_loan', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('interested_in_joining_buzz_plus', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('are_you_happier_than_before', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('do_you_feel_confident_to_solve_your_challenges', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'bdms', ['MonthlyStatus'])


    def backwards(self, orm):
        # Deleting model 'BaseModel'
        db.delete_table(u'bdms_basemodel')

        # Deleting model 'State'
        db.delete_table(u'bdms_state')

        # Deleting model 'District'
        db.delete_table(u'bdms_district')

        # Deleting model 'Block'
        db.delete_table(u'bdms_block')

        # Deleting model 'Place'
        db.delete_table(u'bdms_place')

        # Deleting model 'Partner'
        db.delete_table(u'bdms_partner')

        # Deleting model 'TrainingBatch'
        db.delete_table(u'bdms_trainingbatch')

        # Deleting model 'Trainee'
        db.delete_table(u'bdms_trainee')

        # Deleting model 'MonthlyStatus'
        db.delete_table(u'bdms_monthlystatus')


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
            'are_you_happier_than_before': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'are_you_maintaining_accounts': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bdms.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'difference_between_income_and_profit': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'do_you_feel_confident_to_solve_your_challenges': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'feedback_collected_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'feedback_collected_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_where_did_you_take_a_new_loan': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'have_you_expanded_your_business': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'have_you_started_a_new_business': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'have_you_taken_a_new_loan': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'how_did_you_expanded_your_business': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'how_much_of_your_goals_have_you_reached': ('django.db.models.fields.TextField', [], {}),
            'interested_in_joining_buzz_plus': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'post_training_income': ('django.db.models.fields.IntegerField', [], {}),
            'post_training_profit': ('django.db.models.fields.IntegerField', [], {}),
            'post_training_savings': ('django.db.models.fields.IntegerField', [], {}),
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
            'mobilization_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bdms.Partner']"}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bdms.Place']"}),
            'training_batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bdms.TrainingBatch']"}),
            'training_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'bdms.trainingbatch': {
            'Meta': {'object_name': 'TrainingBatch', '_ormbases': [u'bdms.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['bdms.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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