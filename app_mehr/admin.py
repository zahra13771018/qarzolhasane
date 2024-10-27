from django.contrib import admin
from .models import LoanRequest, Profile, Message, Trans

# ثبت مدل LoanRequest در پنل ادمین
@admin.register(LoanRequest)
class LoanRequestAdmin(admin.ModelAdmin):
    list_display = ('loan_type', 'request_type', 'loan_amount', 'status', 'due_date')
    search_fields = ('loan_type', 'request_type', 'status')
    list_filter = ('status', 'due_date')

# ثبت مدل Profile در پنل ادمین
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'national_id')
    search_fields = ('user__username', 'phone_number', 'national_id')
    list_filter = ('user',)

# ثبت مدل Message در پنل ادمین
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('priority',)

# ثبت مدل Trans در پنل ادمین
@admin.register(Trans)
class TransAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'transaction_type', 'created_at')
    search_fields = ('user__username', 'transaction_type')
    list_filter = ('transaction_type',)

