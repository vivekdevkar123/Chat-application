from django.contrib import admin
from .models import Chat,Group
# Register your models here.

admin.site.register(Chat)
admin.site.register(Group)

class ChatModelAdmin(admin.ModelAdmin):
    list_display = ['chat_id','containt','timestamp','group']

class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['group_id','group_name','created']