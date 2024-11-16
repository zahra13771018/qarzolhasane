# Generated by Django 5.1.1 on 2024-11-16 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mehr', '0004_remove_sandogh_card_number_sandoghcard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='admin_card_info',
            new_name='card_info',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='admin_message_notes',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='allowed_guarantors_count',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='exit_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='guarantor_search',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='national_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pending_messages',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='reminder',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='search_field',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='send_message_field',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_rank',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='withdrawal_operation',
        ),
    ]