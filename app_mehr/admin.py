from django.contrib import admin
<<<<<<< HEAD
from .models import Profile



try:
    admin.site.unregister(Profile)
except admin.sites.NotRegistered:
    pass
=======
from .models import LoanRequest, Trans, Profile, Message

>>>>>>> 261e643f41a1a5280e7867d74b276d56f5fe6f17
    
# @admin.register(CustomUser)
class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'user__is_active', 'user__is_staff')
    search_fields = ('username', 'email')
    exclude = ('national_code', 'father_name', 'mobile_number', 
               'essential_contact_number', 'home_phone', 
               'shaba_number', 'address')

admin.site.register(Profile, ProfileUserAdmin)
# در صورتی که به تنظیمات بیشتری نیاز دارید، می‌توانید آن را در اینجا اضافه کنید.

<<<<<<< HEAD
=======

admin.site.register(LoanRequest)
admin.site.register(Trans)
admin.site.register(Message)

>>>>>>> 261e643f41a1a5280e7867d74b276d56f5fe6f17
