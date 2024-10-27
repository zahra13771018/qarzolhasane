<<<<<<< HEAD
from rest_framework import serializers
from django.test import TestCase
from .models import LoanRequest, Trans, Profile, Message
from .serializers import LoanRequestSerializer, TransSerializer, ProfileSerializer, MessageSerializer


class LoanRequestSerializerTest(TestCase):
    def test_valid_serializer(self):
        data = {
            'field1': 'value1',
            'field2': 'value2',
            # دیگر فیلدهای مورد نیاز
        }
        serializer = LoanRequestSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['field1'], 'value1')

    def test_invalid_serializer(self):
        data = {
            'field1': '',  # فرض کنید این فیلد الزامی است
        }
        serializer = LoanRequestSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('field1', serializer.errors)

class TransSerializerTest(TestCase):
    def test_valid_serializer(self):
        data = {
            'field1': 'value1',
            'field2': 'value2',
            # دیگر فیلدهای مورد نیاز
        }
        serializer = TransSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class ProfileSerializerTest(TestCase):
    def test_valid_serializer(self):
        data = {
            'field1': 'value1',
            'field2': 'value2',
            # دیگر فیلدهای مورد نیاز
        }
        serializer = ProfileSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class MessageSerializerTest(TestCase):
    def test_valid_serializer(self):
        data = {
            'field1': 'value1',
            'field2': 'value2',
            # دیگر فیلدهای مورد نیاز
        }
        serializer = MessageSerializer(data=data)
        self.assertTrue(serializer.is_valid())
=======
from django.test import TestCase

# Create your tests here.
>>>>>>> 261e643f41a1a5280e7867d74b276d56f5fe6f17
