from django.contrib import admin
from home.models import *
# from django.apps import apps

# Register your models here.

admin.site.register(User_profile)
admin.site.register(Form)
admin.site.register(Application)
# admin.site.register(Task)

# class ListAdminMixin(object):
#     def __init__(self, model, admin_site):
#         self.list_display = [field.name for field in model._meta.fields]
#         super(ListAdminMixin, self).__init__(model, admin_site)

# models = apps.get_models()
# for model in models:
#     admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
#     try:
#         admin.site.register(model, admin_class)
#     except admin.sites.AlreadyRegistered:
        # pass