from django.contrib import admin
from .models import AllPost, Comment


class CommentInline(admin.TabularInline): # new
    model = Comment
    extra = 0 

class AllPostAdmin(admin.ModelAdmin): # new
    inlines = [
    CommentInline,
    ]

admin.site.register(AllPost, AllPostAdmin)
admin.site.register(Comment)
