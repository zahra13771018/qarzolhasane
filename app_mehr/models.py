from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings  # برای استفاده از کاربر پیش‌فرض

class Loan(models.Model):
    SHORT_TERM = 'short'
    LONG_TERM = 'long'

    LOAN_TYPE_CHOICES = [
        (SHORT_TERM, 'کوتاه‌مدت'),
        (LONG_TERM, 'بلندمدت'),
    ]

    loan_type = models.CharField(
        max_length=10,
        choices=LOAN_TYPE_CHOICES,
        default=SHORT_TERM,
    )

    def __str__(self):
        return dict(self.LOAN_TYPE_CHOICES).get(self.loan_type, 'نامشخص')

class Deposit(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # حداکثر 10 رقم و 2 رقم اعشار
    date = models.DateField(auto_now_add=True)  # تاریخ واریز به صورت خودکار زمان ایجاد ثبت می‌شود
    loan = models.ForeignKey('Loan', on_delete=models.CASCADE, related_name='deposits')  # ارتباط با مدل Loan

    def __str__(self):
        return f"{self.amount} تومان - {self.date}"


class LoanRequest(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'

    LOAN_STATUS_CHOICES = [
        (PENDING, 'در انتظار بررسی'),
        (APPROVED, 'تایید شده'),
        (REJECTED, 'رد شده'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loan_requests')  # ارتباط با کاربر
    loan_type = models.ForeignKey('Loan', on_delete=models.CASCADE, related_name='loan_requests')  # نوع وام
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # مبلغ درخواست شده
    status = models.CharField(max_length=10, choices=LOAN_STATUS_CHOICES, default=PENDING)  # وضعیت درخواست
    request_date = models.DateTimeField(auto_now_add=True)  # تاریخ ثبت درخواست
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین بروزرسانی

    LOAN_TYPE_CHOICES = [
        ('short', 'کوتاه‌مدت'),
        ('long', 'بلندمدت'),
    ]

    REQUEST_TYPE_CHOICES = [
        ('new', 'درخواست جدید'),
        ('renewal', 'تمدید وام'),
    ]

    STATUS_CHOICES = [
        ('pending', 'در انتظار بررسی'),
        ('approved', 'تایید شده'),
        ('rejected', 'رد شده'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # کاربری که درخواست وام را ارسال کرده
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loan_requests')

    # نوع وام (کوتاه‌مدت یا بلندمدت)
    loan_type = models.CharField(max_length=10, choices=LOAN_TYPE_CHOICES)

    # نوع درخواست (درخواست جدید یا تمدید وام)
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPE_CHOICES)

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

    due_date = models.DateField(null=True, blank=True)  # اضافه کردن فیلد تاریخ سررسید

    def __str__(self):
        return f"{self.user.username} - {self.loan_amount} تومان - {self.get_loan_type_display()} - {self.get_request_type_display()}"


class Trans(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # فیلدهای واریزی و تاریخ‌ها
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')  # کاربر مرتبط
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # اطلاعات شخصی و کارت
    first_name = models.CharField(max_length=100)  # نام
    last_name = models.CharField(max_length=100)  # نام خانوادگی
    father_name = models.CharField(max_length=100)  # نام پدر
    mobile_number = models.CharField(max_length=15)  # شماره موبایل
    emergency_contact = models.CharField(max_length=15, null=True, blank=True)  # شماره تلفن ضروری
    address = models.TextField(null=True, blank=True)  # آدرس
    national_code = models.CharField(max_length=10)  # کد ملی
    card_number = models.CharField(max_length=16)  # شماره کارت بانکی
    shaba_number = models.CharField(max_length=24)  # شماره شبا
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)  # عکس پروفایل
    card_picture = models.ImageField(upload_to='card_pictures/', null=True, blank=True)  # عکس شماره کارت
    national_id_picture = models.ImageField(upload_to='national_ids/', null=True, blank=True)  # عکس کارت ملی
    admin_card_info = models.TextField(null=True, blank=True)  # اطلاعات کارت ادمین
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    national_id = models.CharField(max_length=10, null=True, blank=True)
    guarantor_search = models.CharField(max_length=255, null=True, blank=True)

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

    # متد برای نمایش اطلاعات کاربر
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.mobile_number}"
    
    # متد برای محاسبه تعداد اعضای عضو
    @classmethod
    def get_membership_count(cls):
        return cls.objects.count()
    
class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_messages')  # کاربر ارسال‌کننده پیام
    message_content = models.TextField(max_length=255, default='')  # محتوای پیام پشتیبانی
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ارسال پیام
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین بروزرسانی پیام

    # عنوان پیام
    title = models.CharField(max_length=255)  # عنوان پیام

    # پیام به مدیر صندوق
    message_to_manager = models.TextField()  # پیام به مدیر صندوق

    # پیام مدیر
    manager_message = models.TextField(null=True, blank=True)  # پیام مدیر

    # توضیحات
    description = models.TextField(null=True, blank=True)  # توضیحات پیام

    # پیام درخواست ضامن
    guarantor_request_message = models.TextField(null=True, blank=True)  # پیام درخواست ضامن

    # پیام رد درخواست ضامن
    guarantor_rejection_message = models.TextField(null=True, blank=True)  # پیام رد درخواست ضامن

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    # توضیحات مدیر صندوق
    manager_description = models.TextField(null=True, blank=True)  # توضیحات مدیر صندوق

    # اولویت تیکت ارسال پیام
    PRIORITY_CHOICES = [
        ('low', 'کم'),
        ('medium', 'متوسط'),
        ('high', 'زیاد'),
    ]
    ticket_priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')  # اولویت تیکت

    def __str__(self):
        return f"Message: {self.title} (Priority: {self.ticket_priority})"

