from django.contrib import admin
from mysite.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','pub_date') #管理欄位
admin.site.register(Post, PostAdmin)