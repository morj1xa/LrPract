# -*- coding: utf-8 -*-
import unittest
from myform import validate_order

class TestValidateOrder(unittest.TestCase):
    def test_valid_order(self):
        # ��������� ���������� �����
        self.assertIsNone(validate_order("John", "Order details", "+7 123 456 78 90", "2024-05-22"))

    def test_invalid_name(self):
        # ��������� ������������ ��� (� �������)
        self.assertEqual(validate_order("John123", "Order details", "+7 123 456 78 90", "2024-05-22"),
                         "Name should contain only English letters and no digits!")

    def test_invalid_text_length(self):
        # ��������� ������������ ����� ������ (������ 3 ��������)
        self.assertEqual(validate_order("John", "Te", "+7 123 456 78 90", "2024-05-22"),
                         "Text should be at least 3 characters long!")

    def test_invalid_phone_format(self):
        # ��������� ������������ ������ ��������
        self.assertEqual(validate_order("John", "Order details", "1234567890", "2024-05-22"),
                         "Phone format should be like: +7 000 000 00 00!")

    def test_invalid_date(self):
        # ��������� ������������ ���� (����� ������� ����)
        self.assertEqual(validate_order("John", "Order details", "+7 123 456 78 90", "2025-05-22"),
                         "Date should not be greater than today!")

if __name__ == '__main__':
    unittest.main()
