# from django.contrib import admin
# from .models import LoanRequest, Profile, Message, Trans

# # ثبت مدل LoanRequest در پنل ادمین
# @admin.register(LoanRequest)
# class LoanRequestAdmin(admin.ModelAdmin):
#     list_display = ('loan_type', 'request_type', 'loan_amount', 'status', 'due_date')
#     search_fields = ('loan_type', 'request_type', 'status')
#     list_filter = ('status', 'due_date')

# # ثبت مدل Profile در پنل ادمین
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'phone_number', 'national_id')
#     search_fields = ('user__username', 'phone_number', 'national_id')
#     list_filter = ('user',)

# # ثبت مدل Message در پنل ادمین
# @admin.register(Message)
# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'priority', 'created_at')
#     search_fields = ('title', 'description')
#     list_filter = ('priority',)

# # ثبت مدل Trans در پنل ادمین
# @admin.register(Trans)
# class TransAdmin(admin.ModelAdmin):
#     list_display = ('user', 'amount', 'transaction_type', 'created_at')
#     search_fields = ('user__username', 'transaction_type')
#     list_filter = ('transaction_type',)



# # admin.py
# from django.contrib import admin
# from .models import Message, Profile, Trans

# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'priority')  # اطمینان از وجود priority
#     list_filter = ('priority',)

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'phone_number', 'national_id')  # اطمینان از وجود phone_number و national_id

# class TransAdmin(admin.ModelAdmin):
#     list_display = ('id', 'amount', 'transaction_type', 'created_at')  # اطمینان از وجود این فیلدها
#     list_filter = ('transaction_type',)

# admin.site.register(Message, MessageAdmin)
# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Trans, TransAdmin)


# from django.contrib import admin
# from .models import Message, Profile, Trans

# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'priority')  # اطمینان از وجود priority
#     list_filter = ('priority',)

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'phone_number', 'national_id')  # اطمینان از وجود phone_number و national_id

# class TransAdmin(admin.ModelAdmin):
#     list_display = ('id', 'amount', 'transaction_type', 'created_at')  # اطمینان از وجود این فیلدها
#     list_filter = ('transaction_type',)

# # فقط یک بار ثبت مدل‌ها
# admin.site.register(Message, MessageAdmin)
# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Trans, TransAdmin)


# app_mehr/admin.py

from django.contrib import admin
from .models import Message, Profile, Trans

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'ticket_priority')  # تغییر 'priority' به 'ticket_priority'
    list_filter = ('ticket_priority',)  # تغییر 'priority' به 'ticket_priority'

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'mobile_number', 'national_code')  # تغییر نام فیلدها
    list_filter = ('national_code',)  # اگر بخواهی فیلتر براساس کد ملی داشته باشی

class TransAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'deposit_amount', 'status', 'last_updated')  # تغییر نام فیلدها
    list_filter = ('status', 'deposit_amount')  # استفاده از فیلدهای موجود

admin.site.register(Message, MessageAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Trans, TransAdmin)
