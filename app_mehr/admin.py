from django.contrib import admin
from .models import Message, Profile, Trans, LoanRequest

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'ticket_priority')
    list_filter = ('ticket_priority',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'mobile_number', 'national_code')
    list_filter = ('national_code',)

class TransAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'deposit_amount', 'status', 'deposit_date', 'deposit_status', 'fund_balance')
    list_filter = ('status', 'deposit_status', 'deposit_date')

class LoanRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'loan_amount', 'loan_type', 'request_type', 'status', 'request_date', 'updated_at')
    list_filter = ('status', 'loan_type', 'request_type')  # اضافه کردن فیلترها

admin.site.register(Message, MessageAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Trans, TransAdmin)
admin.site.register(LoanRequest, LoanRequestAdmin)


