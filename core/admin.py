from django.contrib import admin

from .models import GitUser, Data, Group

admin.site.register(GitUser)
admin.site.register(Data)
admin.site.register(Group)