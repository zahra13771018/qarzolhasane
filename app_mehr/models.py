# from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.models import User
from django.db import models



class LoanRequest(models.Model):

    LOAN_TYPE_CHOICES =(
        ("essential", 'ضروری'),
        ("normal" , 'معمولی'),
        
    )

    REQUEST_TYPE_CHOICES =(
        ("renewal", 'تمدید وام'),
        ("new", 'درخواست جدید'),
        
    )

    STATUS_CHOICES = (
        ('pending', 'در انتظار بررسی'),
        ('approved', 'تایید شده'),
        ('rejected', 'رد شده'),
    )

    # کاربری که درخواست وام را ارسال کرده
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loan_requests')

    # نوع وام (کوتاه‌مدت یا بلندمدت)
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPE_CHOICES)

    # نوع درخواست (درخواست جدید یا تمدید وام)
    request_type = models.CharField(max_length=7, choices=REQUEST_TYPE_CHOICES)

    # مبلغ وام درخواستی
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # مبلغ واریز شده برای وام
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # وضعیت درخواست (در انتظار بررسی، تایید شده یا رد شده)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    # تاریخ ثبت درخواست
    request_date = models.DateTimeField(auto_now_add=True)

    # تاریخ آخرین بروزرسانی وضعیت درخواست
    updated_at = models.DateTimeField(auto_now=True)

     # تاریخ سررسید
    due_date = models.DateField(default='2024-01-01')  # تاریخ سررسید قسط

    # شماره قسط
    installment_number = models.PositiveSmallIntegerField(default=0)  # شماره قسط

    # مجموع مبلغ واریزی
    total_deposit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # مجموع مبلغ واریزی

    # ردیف
    rank = models.PositiveSmallIntegerField(default=1)  #  ردیف یا رتبه


    def __str__(self):
        return f"{self.user.username} - {self.loan_amount} تومان - {self.get_loan_type_display()} - {self.get_request_type_display()}"
    





class Trans(models.Model):

    # عنوان
    title = models.CharField(max_length=300, default="بدون عنوان")  # عنوان تراکنش

    # مبلغ بدهی
    debt_amount = models.DecimalField(max_digits=12, decimal_places=2)  # مبلغ بدهی

    # وضعیت
    STATUS_CHOICES = [
        ('pending', 'در انتظار'),
        ('paid', 'پرداخت شده'),
        ('unpaid', 'پرداخت نشده'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # وضعیت پرداخت

    # تایید مدیر
    manager_approval = models.BooleanField(default=False)  # تایید مدیر

    # آپلود فیش واریزی
    receipt_upload = models.ImageField(upload_to='receipts/', null=True, blank=True)  # آپلود فیش واریزی

    # مبلغ پرداخت
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # مبلغ پرداخت

    # توضیحات
    description = models.TextField(null=True, blank=True)  # توضیحات

    # صورت‌حساب پرداخت شما
    payment_statement = models.TextField(null=True, blank=True)  # صورت‌حساب پرداخت

    # فیلدهای واریزی و تاریخ‌ها
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')  # کاربر مرتبط
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)  # رسید فیش
    deposit_status = models.CharField(max_length=20, choices=[('pending', 'در انتظار'), ('confirmed', 'تایید شده'), ('rejected', 'رد شده')], default='pending')  # وضعیت واریز
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # مبلغ واریز
    deposit_date = models.DateTimeField(null=True, blank=True)  # تاریخ واریز
    receipt_date = models.DateTimeField(null=True, blank=True)  # تاریخ رسید فیش
    
    # نمودار 6 ماهه صندوق و موجودی
    six_month_chart_data = models.JSONField(null=True, blank=True)  # داده‌های نمودار 6 ماه اول صندوق (به صورت JSON ذخیره می‌شود)
    fund_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)  # موجودی صندوق

    # تعداد اقساط
    paid_installments = models.PositiveIntegerField(default=0)  # تعداد اقساط تسویه شده
    unpaid_installments = models.PositiveIntegerField(default=0)  # تعداد اقساط تسویه نشده

    # صورت‌حساب و بدهی‌ها
    payment_statement = models.TextField(null=True, blank=True)  # صورت حساب پرداخت کاربر
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # بدهی کاربر
    
    # حق اشتراک و تعداد وام‌های مجاز
    subscription_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # مبلغ حق اشتراک
    allowed_loans_count = models.PositiveIntegerField(default=0)  # تعداد وام‌های مجاز برای هر کاربر
    
    # تاریخ‌ها و درخواست‌ها
    request_date = models.DateTimeField(auto_now_add=True)  # تاریخ درخواست
    last_updated = models.DateTimeField(auto_now=True)  # تاریخ آخرین بروزرسانی

    # کاربران و واریزی‌ها
    has_paid_this_month = models.BooleanField(default=False)  # آیا کاربر در این ماه واریز کرده؟
    
    def __str__(self):
        return f"{self.user.username} - {self.deposit_amount} تومان - {self.get_deposit_status_display()}"
    
    # متد برای مشاهده کاربران پرداخت کرده و نکرده
    @classmethod
    def get_users_paid_this_month(cls):
        return cls.objects.filter(has_paid_this_month=True)
    
    @classmethod
    def get_users_not_paid_this_month(cls):
        return cls.objects.filter(has_paid_this_month=False)
    


class Profile(models.Model):
    # اطلاعات شخصی و کارت
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # ارتباط با مدل کاربر
    first_name = models.CharField(max_length=100, default="")  # نام
    last_name = models.CharField(max_length=100, default="")  # نام خانوادگی
    father_name = models.CharField(max_length=100)  # نام پدر
    mobile_number = models.CharField(max_length=15, default="")  # شماره موبایل
    emergency_contact = models.CharField(max_length=15, null=True, blank=True)  # شماره تلفن ضروری
    address = models.TextField(null=True, blank=True)  # آدرس
    national_code = models.CharField(max_length=10, default="")  # کد ملی
    card_number = models.CharField(max_length=16, default='0')  # شماره کارت بانکی
    shaba_number = models.CharField(max_length=24, default="")  # شماره شبا
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)  # عکس پروفایل
    card_picture = models.ImageField(upload_to='card_pictures/', null=True, blank=True)  # عکس شماره کارت
    national_id_picture = models.ImageField(upload_to='national_ids/', null=False, default='')  # عکس کارت ملی
    admin_card_info = models.TextField(null=True, blank=True)  # اطلاعات کارت ادمین

    # تاریخ و ردیف
    exit_date = models.DateField(null=True, blank=True)  # تاریخ خروج
    user_rank = models.PositiveIntegerField(null=True, blank=True)  # ردیف یا رتبه کاربر

    # فیلدهای مرتبط با پیام و یادآوری
    pending_messages = models.TextField(null=True, blank=True)  # پیام‌های در انتظار پاسخ
    send_message_field = models.TextField(null=True, blank=True)  # فیلد خالی برای ارسال پیام
    admin_message_notes = models.TextField(null=True, blank=True)  # توضیحات پیام ادمین به کاربر
    reminder = models.CharField(max_length=255, null=True, blank=True)  # یادآوری برای کاربر
    allowed_guarantors_count = models.PositiveIntegerField(default=0)  # تعداد مجاز ضامن برای هر کاربر

    # عملیات انصراف
    withdrawal_operation = models.BooleanField(default=False)  # عملیات انصراف

    # فیلد جستجو
    search_field = models.JSONField(null=True, blank=True)  # فیلد جستجو به صورت لیست (ذخیره به صورت JSON)

  # تلفن منزل
    home_phone = models.CharField(max_length=15, default="بدون شماره")  # تلفن منزل

    # آپلود عکس کارت ملی
    national_id_picture = models.ImageField(upload_to='national_ids/', null=False, default='path/to/default/image.jpg')  # آپلود عکس کارت ملی

    # آپلود عکس پروفایل
    profile_picture = models.ImageField(upload_to='profiles/', null=False, default='path/to/default/image.jpg')  # آپلود عکس پروفایل

    # فیلد جستجوی ضامن (به صورت لیست JSON)
    guarantor_search = models.JSONField(null=True, blank=True)  # فیلد جستجوی ضامن

    # انصراف از صندوق
    withdraw_from_fund = models.BooleanField(default=False)  # انصراف از صندوق

    # متد برای نمایش اطلاعات کاربر
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.mobile_number}"
    
    # متد برای محاسبه تعداد اعضای عضو
    @classmethod
    def get_membership_count(cls):
        return cls.objects.count()


class Message(models.Model):
    # عنوان پیام
    title = models.CharField(max_length=255, default="بدون عنوان")  # عنوان پیام

    # پیام به مدیر صندوق
    message_to_manager = models.TextField(default="")  # پیام به مدیر صندوق

    # پیام مدیر
    manager_message = models.TextField(null=True, blank=True)  # پیام مدیر

    # توضیحات
    description = models.TextField(null=True, blank=True)  # توضیحات پیام

    # پیام درخواست ضامن
    guarantor_request_message = models.TextField(null=True, blank=True)  # پیام درخواست ضامن

    # پیام رد درخواست ضامن
    guarantor_rejection_message = models.TextField(null=True, blank=True)  # پیام رد درخواست ضامن

    # توضیحات مدیر صندوق
    manager_description = models.TextField(null=True, blank=True)  # توضیحات مدیر صندوق

    # اولویت تیکت ارسال پیام
    PRIORITY_CHOICES = [
        ('low', 'کم'),
        ('medium', 'متوسط'),
        ('high', 'زیاد'),
    ]
    ticket_priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')  # اولویت تیکت
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_messages')  # کاربر ارسال‌کننده پیام
    message_content = models.TextField()  # محتوای پیام پشتیبانی
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ارسال پیام
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین بروزرسانی پیام

    def __str__(self):
        return f"پیام از {self.user.username} - تاریخ: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"