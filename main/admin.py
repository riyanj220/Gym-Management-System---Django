from django.contrib import admin
from . import models

class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text','image_tag')
admin.site.register(models.Banners,BannerAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(models.Service,ServiceAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(models.Page,PageAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question',)
admin.site.register(models.Faq,FaqAdmin)


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name','query','email','send_time')
admin.site.register(models.Enquiry,EnquiryAdmin)



