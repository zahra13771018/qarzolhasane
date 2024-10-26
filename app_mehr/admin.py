from django.contrib import admin
from .models import LoanRequest, Trans, Profile, Message

    
# @admin.register(CustomUser)
class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'user__is_active', 'user__is_staff')
    search_fields = ('username', 'email')
    exclude = ('national_code', 'father_name', 'mobile_number', 
               'essential_contact_number', 'home_phone', 
               'shaba_number', 'address')

admin.site.register(Profile, ProfileUserAdmin)
# در صورتی که به تنظیمات بیشتری نیاز دارید، می‌توانید آن را در اینجا اضافه کنید.


admin.site.register(LoanRequest)
admin.site.register(Trans)
admin.site.register(Message)

