from .models import *
from django.contrib import admin

#This needs to be extended with perms
def can_add(user):
    groups = [x.name for x in user.groups.all() ]
    return ( user.is_superuser or "Founder" in groups or  "Manager" in groups or "Coordinator" in groups or "Trainer" in groups)

def can_change(user):
    groups = [x.name for x in user.groups.all() ]
    return ( user.is_superuser or "Founder" in groups or "Manager" in groups or "Coordinator" in groups or "Trainer" in groups)

def can_delete(user):
    groups = [x.name for x in user.groups.all() ]
    return ( user.is_superuser or "Founder" in groups or "Manager" in groups  ) 


def can_read(user):
    return True

def bdms_set_attr(obj,attr,val):
        if hasattr(obj,attr):
            setattr(obj,attr,val)


class BaseAdmin(admin.ModelAdmin):
    qs_extra_params = {}
    csv_export_fields = { 'include' : None, 'fields' : None, 'exclude' : None}
    def save_model(self, request, obj, form, change):
        if not obj.id:
            bdms_set_attr(obj,'created_by_id',request.user.id)
        bdms_set_attr(obj,'last_edited_by_id',request.user.id)
        obj.save()

    def has_add_permission(self, request,obj=None):
        return can_add(request.user)
 
    def has_delete_permission(self, request,obj=None):
        return can_delete(request.user)

    def change_view(self, request, object_id, extra_context=None):
        if not can_change(request.user):
            self.readonly_fields=self.user_readonly
            self.inlines = self.user_readonly_inlines
 
        try:
            return super(BaseAdmin, self).change_view(
                request, object_id, extra_context=extra_context)
        except PermissionDenied:
            pass
        if request.method == 'POST':
            raise PermissionDenied
        request.readonly = True
        return super(BaseAdmin, self).change_view(
            request, object_id, extra_context=extra_context)

    def get_actions(self, request):
        actions = super(BaseAdmin, self).get_actions(request)
        if 'delete_selected' in actions and not can_delete(request.user):
           del actions['delete_selected']
        return actions

    def save_formset(self, request, form, formset, change):
        instances=formset.save(commit=False)
        for obj in instances:
            if not obj.id:
                bdms_set_attr(obj,'created_by_id',request.user.id)
            bdms_set_attr(obj,'last_edited_by_id',request.user.id)
            obj.save()
        formset.save_m2m()





class StateAdmin(BaseAdmin):
    model = State
    user_readonly = ['name']
    user_readonly_inlines = []

class DistrictAdmin(BaseAdmin):
    model = District
    user_readonly = ['name','state']
    user_readonly_inlines = []

class BlockAdmin(BaseAdmin):
    model = Block
    user_readonly = ['name','district']
    user_readonly_inlines = []

class PlaceAdmin(BaseAdmin):
    model = Place
    user_readonly = ['name','block']
    user_readonly_inlines = []

class TrainingBatchAdmin(BaseAdmin):
    model = TrainingBatch
    user_readonly = ['name','block']
    user_readonly_inlines = []

class PartnerAdmin(BaseAdmin):
    model = Partner
    user_readonly = ['name']
    user_readonly_inlines = []


class MonthlyStatusAdmin(BaseAdmin):
    model = MonthlyStatus
    list_display = ('id','trainee','training_date','feedback_collected_date','feedback_collected_by')
    user_readonly = ['age','place','partner','mobilization_date','training_date','training_batch','literacy_level','business','contact_mobile','current_monthly_income','current_monthly_profit','current_monthly_savings','current_challenges']
    user_readonly_inlines = []

    def training_date(self,obj):
        return obj.trainee.training_date

class TraineeAdmin(BaseAdmin):
    list_display = ('id','name','age','place','partner','mobilization_date','training_date')
    list_filter = ('partner',)
    user_readonly = ['trainee','feedback_collected_date','feedback_collected_by','post_training_income','post_training_profit','post_training_savings','difference_between_income_and_profit','are_you_maintaining_accounts','how_much_of_your_goals_have_you_reached','have_you_started_a_new_business','have_you_expanded_your_business','how_did_you_expanded_your_business','have_you_taken_a_new_loan','from_where_did_you_take_a_new_loan','interested_in_joining_buzz_plus','are_you_happier_than_before','do_you_feel_confident_to_solve_your_challenges']
    user_readonly_inlines = []
    model = Trainee

admin.site.register(State, StateAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Place, PlaceAdmin)

admin.site.register(Partner, PartnerAdmin)
admin.site.register(TrainingBatch, TrainingBatchAdmin)
admin.site.register(Trainee, TraineeAdmin)
admin.site.register(MonthlyStatus, MonthlyStatusAdmin)
