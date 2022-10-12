from django.contrib import admin

from .models import Stories, StoriesView, Contact ,institute_deatil

admin.site.register(Stories)
admin.site.register(institute_deatil)
admin.site.register(StoriesView)
admin.site.register(Contact)