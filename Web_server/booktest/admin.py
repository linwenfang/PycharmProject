from django.contrib import admin
from .models import BookInfo,DetailInfo
# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title','pub_date']
class DetailInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','content','people','gender']
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(DetailInfo,DetailInfoAdmin)