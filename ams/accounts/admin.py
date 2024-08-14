from django.contrib import admin
from .models import Rank, Profile, Document, BankDetail, Device

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'phone_number', 'designation', 'rank', 'gender', 'address', 'profile_image')
    search_fields = ('user__username', 'phone_number', 'designation', 'address')
    list_filter = ('rank', 'gender')

class RankAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'citizenship_number', 'issued_date', 'issued_district', 'pan_number')
    search_fields = ('user__username', 'citizenship_number', 'pan_number')
    list_filter = ('issued_date',)

class BankDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank_name', 'bank_account', 'bank_account_name', 'bank_branch')
    search_fields = ('user__username', 'bank_name', 'bank_account')
    list_filter = ('bank_name',)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'device_id', 'fingerprint_id')
    search_fields = ('user__username', 'device_id', 'fingerprint_id')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(BankDetail, BankDetailAdmin)
admin.site.register(Device, DeviceAdmin)
