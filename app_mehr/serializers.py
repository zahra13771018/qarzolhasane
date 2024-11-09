from rest_framework import serializers
from .models import LoanRequest, Profile, Message, Trans, Sandogh, SandoghCard


class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = [
            'id',
            'user',  # کاربر درخواست کننده
            'loan_type',
            'request_type',
            'loan_amount',
            'deposit_amount',
            'status',
            'request_date',  # تاریخ ثبت درخواست
            'updated_at',  # تاریخ آخرین بروزرسانی
            'due_date'  # تاریخ سررسید
        ]
        read_only_fields = ['id', 'user', 'request_date', 'updated_at']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'user',  # کاربر مربوطه
            'first_name',
            'last_name',  # نام خانوادگی
            'father_name',  # نام پدر
            'mobile_number',  # شماره موبایل
            'emergency_contact',  # شماره تماس ضروری
            'address',  # آدرس
            'national_code',  # کد ملی
            'card_number',  # شماره کارت بانکی
            'shaba_number',  # شماره شبا
            'profile_picture',  # عکس پروفایل
            'card_picture',  # عکس کارت بانکی
            'national_id_picture',  # عکس کارت ملی
            'admin_card_info',  # اطلاعات کارت ادمین
            'phone_number',  # شماره تلفن
            'national_id',  # کد ملی
            'guarantor_search',  # فیلد جستجوی ضامن
            'exit_date',  # تاریخ خروج
            'user_rank',  # رتبه کاربر
            'pending_messages',  # پیام‌های در انتظار
            'send_message_field',  # فیلد ارسال پیام
            'admin_message_notes',  # یادداشت‌های ادمین
            'reminder',  # یادآوری
            'allowed_guarantors_count',  # تعداد مجاز ضامن
            'withdrawal_operation',  # عملیات انصراف
            'search_field',  # فیلد جستجو
        ]
        read_only_fields = ['id', 'user']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'user',  # کاربر ارسال‌کننده
            'message_content',  # محتوای پیام
            'created_at',  # تاریخ ارسال پیام
            'updated_at',  # تاریخ آخرین بروزرسانی
            'title',  # عنوان پیام
            'message_to_manager',  # پیام به مدیر
            'manager_message',  # پیام مدیر
            'description',  # توضیحات
            'guarantor_request_message',  # پیام درخواست ضامن
            'guarantor_rejection_message',  # پیام رد درخواست ضامن
            'manager_description',  # توضیحات مدیر صندوق
            'ticket_priority',  # اولویت تیکت
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class TransSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trans
        fields = [
            'id',
            'user',  # کاربر مرتبط
            'title',  # عنوان تراکنش
            'status',  # وضعیت تراکنش
            'receipt',  # رسید فیش
            'deposit_status',  # وضعیت واریز
            'deposit_amount',  # مبلغ واریز
            'deposit_date',  # تاریخ واریز
            'receipt_date',  # تاریخ رسید فیش
            'six_month_chart_data',  # داده‌های نمودار 6 ماه
            'fund_balance',  # موجودی صندوق
            'paid_installments',  # تعداد اقساط پرداخت شده
            'unpaid_installments',  # تعداد اقساط پرداخت نشده
            'payment_statement',  # صورت‌حساب پرداخت
            'debt_amount',  # بدهی
            'subscription_fee',  # مبلغ حق اشتراک
            'allowed_loans_count',  # تعداد وام‌های مجاز
            'request_date',  # تاریخ درخواست
            'last_updated',  # تاریخ آخرین بروزرسانی
            'has_paid_this_month',  # آیا در این ماه پرداخت شده؟
        ]
        read_only_fields = ['id', 'user']


class SandoghCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SandoghCard
        fields = '__all__'


class SandoghSerializer(serializers.ModelSerializer):
    cards = SandoghCardSerializer(
        many=True, read_only=True, source='sandoghcard_set')

    class Meta:
        model = Sandogh
        fields = '__all__'
