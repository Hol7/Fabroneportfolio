from django.contrib import admin

# Register your models here.

from .models import Project, Skill, Tag, Message, Endoresment, Comment

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Message)
admin.site.register(Endoresment)
admin.site.register(Comment)