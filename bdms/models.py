from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
import urlparse
from jsonfield import JSONField
from django.core import serializers
from collections import OrderedDict
from django.contrib.auth.models import User


LITERACY_LEVEL_CHOICES = (
    ('Graduate','Graduate'),
    ('High School','High School'),
    ('Read and Write', 'Read and Write'),
    ('Can sign','Can sign'),
    ('Illiterate','Illiterate'),    
)

class BaseModel(models.Model):
    created_by = models.ForeignKey(User,verbose_name='user',editable=False,related_name='%(app_label)s_%(class)s_created_set')
    last_edited_by = models.ForeignKey(User,editable=False,related_name='%(app_label)s_%(class)s_edited_set')
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)



class State(BaseModel):
    name =  models.CharField(max_length=50, null=False,editable=True)
    def __unicode__(self):
        return u'%s' % (self.name)

class District(BaseModel):
    name =  models.CharField(max_length=50, null=False,editable=True)
    state = models.ForeignKey(State)

    def __unicode__(self):
        return u'%s, %s' % (self.name, self.state.name)

class Block(BaseModel):
    name =  models.CharField(max_length=50, null=False,editable=True)
    district = models.ForeignKey(District)

    def __unicode__(self):
        return u'%s, %s' % (self.name, self.district)


class Place(BaseModel): 
    name =  models.CharField(max_length=50, null=False,editable=True)
    block = models.ForeignKey(Block)

    def __unicode__(self):
        return u'%s, %s' % (self.name, self.block)
    

class Partner(BaseModel): 
    name =  models.CharField(max_length=100, null=False,editable=True)
    def __unicode__(self):
        return u'%s' % (self.name)


class TrainingBatch(BaseModel):
    name =  models.CharField(max_length=50, null=False,editable=True)

    def __unicode__(self):
        return u'%s' % (self.name)

class Trainee(BaseModel):
    name                        = models.CharField(max_length=100, null=False,editable=True)
    age                         = models.IntegerField(default=20);
    place                       = models.ForeignKey(Place)
    partner                     = models.ForeignKey(Partner)
    mobilization_date           = models.DateField(blank=True,null=True,auto_now_add=True,editable=True)
    training_date               = models.DateField(blank=True,null=True,auto_now_add=True,editable=True)
    training_batch              = models.ForeignKey(TrainingBatch)
    literacy_level              = models.CharField(max_length=20,null=True,choices=LITERACY_LEVEL_CHOICES,default='Illiterate')
    business                    = models.TextField(blank=True,null=True,editable=True)
    contact_mobile              = models.CharField(blank=True,null=True,max_length=10,editable=True)
    current_monthly_income      = models.IntegerField(blank=True,null=True,editable=True)
    current_monthly_profit      = models.IntegerField(blank=True,null=True,editable=True)
    current_monthly_savings     = models.IntegerField(blank=True,null=True,editable=True)
    current_challenges          = models.TextField(blank=True,null=True,editable=True)

    def __unicode__(self):
        return u'%s, %s' % (self.trainee.name, self.trainee.place)



class MonthlyStatus(BaseModel):
    # Update to GenericIPAddress in Django 1.4
    trainee                                         = models.ForeignKey(Trainee)
    feedback_collected_date                         = models.DateField(auto_now_add=True,editable=True)
    feedback_collected_by                           = models.ForeignKey(User)
    post_training_income                            = models.IntegerField(editable=True)
    post_training_profit                            = models.IntegerField(editable=True)
    post_training_savings                           = models.IntegerField(editable=True)
    difference_between_income_and_profit            = models.CharField(max_length=20,choices=(('Answered','Answered'),('Could not Answer',' Could not Answer'),) )
    are_you_maintaining_accounts                    = models.CharField(max_length=20,choices=(('Everyday','Everyday'),('Sometimes',' Sometimes'),('No','No'),) )
    how_much_of_your_goals_have_you_reached         = models.TextField(editable=True)
    have_you_started_a_new_business                 = models.CharField(max_length=20,choices=(('Yes','Yes'),('No','No'),('Already had business','Already had business'),('Dont plan to start','Dont plan to start'),) )    
    have_you_expanded_your_business                 = models.CharField(max_length=5,choices=(('Yes','Yes'),('No','No'),) )
    how_did_you_expanded_your_business              = models.CharField(max_length=20,choices=(('Added more capital','Added more capital'),('Added more staff','Added more staff'),('Added new products','Added new products'),('Added new markets','Added new markets'),) )
    have_you_taken_a_new_loan                       = models.CharField(max_length=5,choices=(('Yes','Yes'),('No','No'),) )
    from_where_did_you_take_a_new_loan              = models.CharField(max_length=20,choices=(('Bank','Bank'),('Relatives','Relatives'),) )
    interested_in_joining_buzz_plus                 = models.CharField(max_length=5,choices=(('Yes','Yes'),('No','No'),) )
    are_you_happier_than_before                     = models.CharField(max_length=5,choices=(('Yes','Yes'),('No','No'),('Maybe','Maybe'),) )
    do_you_feel_confident_to_solve_your_challenges  = models.CharField(max_length=5,choices=(('Yes','Yes'),('No','No'),('Maybe','Maybe'),) )

    def __unicode__(self):
        return u'%s, %s' % (self.trainee.name, self.feedback_collected_date)
