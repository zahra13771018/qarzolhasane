from django.contrib.auth.models import User
from django.db import models

class LoanRequest(models.Model):
    LOAN_TYPE_CHOICES = (
        ("essential", 'ضروری'),
        ("normal", 'معمولی'),
    )

    REQUEST_TYPE_CHOICES = (
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
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPE_CHOICES)
    request_type = models.CharField(max_length=7, choices=REQUEST_TYPE_CHOICES)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    request_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(default='2024-01-01')
    installment_number = models.PositiveSmallIntegerField(default=0)
    total_deposit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rank = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.loan_amount} تومان - {self.get_loan_type_display()} - {self.get_request_type_display()}"

class Trans(models.Model):
    title = models.CharField(max_length=300, default="بدون عنوان")
    debt_amount = models.DecimalField(max_digits=12, decimal_places=2)
    
    STATUS_CHOICES = [
        ('pending', 'در انتظار'),
        ('paid', 'پرداخت شده'),
        ('unpaid', 'پرداخت نشده'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    manager_approval = models.BooleanField(default=False)
    receipt_upload = models.ImageField(upload_to='receipts/', null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(null=True, blank=True)
    payment_statement = models.TextField(null=True, blank=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    deposit_status = models.CharField(max_length=20, choices=[('pending', 'در انتظار'), ('confirmed', 'تایید شده'), ('rejected', 'رد شده')], default='pending')
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deposit_date = models.DateTimeField(null=True, blank=True)
    receipt_date = models.DateTimeField(null=True, blank=True)
    
    six_month_chart_data = models.JSONField(null=True, blank=True)
    fund_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    paid_installments = models.PositiveIntegerField(default=0)
    unpaid_installments = models.PositiveIntegerField(default=0)
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subscription_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    allowed_loans_count = models.PositiveIntegerField(default=0)
    request_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    has_paid_this_month = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.deposit_amount} تومان - {self.get_deposit_status_display()}"

    @classmethod
    def get_users_paid_this_month(cls):
        return cls.objects.filter(has_paid_this_month=True)
    
    @classmethod
    def get_users_not_paid_this_month(cls):
        return cls.objects.filter(has_paid_this_month=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    father_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, default="")
    emergency_contact = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    national_code = models.CharField(max_length=10, default="")
    card_number = models.CharField(max_length=16, default='0')
    shaba_number = models.CharField(max_length=24, default="")
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    card_picture = models.ImageField(upload_to='card_pictures/', null=True, blank=True)
    national_id_picture = models.ImageField(upload_to='national_ids/', null=False, default='')
    admin_card_info = models.TextField(null=True, blank=True)
    exit_date = models.DateField(null=True, blank=True)
    user_rank = models.PositiveIntegerField(null=True, blank=True)
    pending_messages = models.TextField(null=True, blank=True)
    send_message_field = models.TextField(null=True, blank=True)
    admin_message_notes = models.TextField(null=True, blank=True)
    reminder = models.CharField(max_length=255, null=True, blank=True)
    allowed_guarantors_count = models.PositiveIntegerField(default=0)
    withdrawal_operation = models.BooleanField(default=False)
    search_field = models.JSONField(null=True, blank=True)
    home_phone = models.CharField(max_length=15, default="بدون شماره")
    guarantor_search = models.JSONField(null=True, blank=True)
    withdraw_from_fund = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.mobile_number}"
    
    @classmethod
    def get_membership_count(cls):
        return cls.objects.count()

class Message(models.Model):
    title = models.CharField(max_length=255, default="بدون عنوان")
    message_to_manager = models.TextField(default="")
    manager_message = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    guarantor_request_message = models.TextField(null=True, blank=True)
    guarantor_rejection_message = models.TextField(null=True, blank=True)
    manager_description = models.TextField(null=True, blank=True)
    
    PRIORITY_CHOICES = [
        ('low', 'کم'),
        ('medium', 'متوسط'),
        ('high', 'زیاد'),
    ]
    ticket_priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_messages')
    message_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"پیام از {self.user.username} - تاریخ: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
