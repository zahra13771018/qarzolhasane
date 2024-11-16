import random
from django.core.management.base import BaseCommand
from faker import Faker
from app_mehr.models import Profile  # نام مدل صحیح را وارد کنید

class Command(BaseCommand):
    help = "Populate the database with fake data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(50):  
            Profile.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                father_name=fake.first_name(), 
                mobile_number=fake.phone_number(), 
                emergency_contact=fake.phone_number(),  
                address=fake.address(),
                national_code=fake.unique.random_number(digits=10),  
                card_number=fake.credit_card_number(),  
                shaba_number=fake.iban(),  
                
                profile_picture="path/to/default/profile.jpg",
                card_picture="path/to/default/card.jpg",
                national_id_picture="path/to/default/national_id.jpg",
                card_info=fake.credit_card_full()
            )
        self.stdout.write(self.style.SUCCESS("Database populated with fake data successfully."))

