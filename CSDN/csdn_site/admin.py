from django.contrib import admin

# Register your models here.
from csdn_site import models


class DataAdmin(admin.ModelAdmin):
    list_display = ('csdn_article_name', 'num_likes')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)


admin.site.register(models.Data, DataAdmin)
admin.site.register(models.CsdnUser, UserAdmin)
