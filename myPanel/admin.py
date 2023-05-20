from django.contrib import admin

from myPanel.models import BlogPost,Messages

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Messages)