import unittest
from myform import add_order  # ���������� ����� ��� ������ ������ ��� ����� � �������� add_order

class TestAddOrder(unittest.TestCase):
    def test_name_validation(self):
        # �������� ����� �� ���������� ����� � ���������� ����
        self.assertEqual(add_order('123', 'text', '+7 000 000 00 00', '2024-05-22'), "Name should contain only English letters and no digits!")
        self.assertEqual(add_order('name', 'text', '+7 000 000 00 00', '2024-05-22'), None)

    def test_text_length(self):
        # �������� ������ �� ����� �� ����� 3 ��������
        self.assertEqual(add_order('name', 'te', '+7 000 000 00 00', '2024-05-22'), "Text should be at least 3 characters long!")
        self.assertEqual(add_order('name', 'text', '+7 000 000 00 00', '2024-05-22'), None)

    def test_phone_format(self):
        # �������� ������� ��������
        self.assertEqual(add_order('name', 'text', '1234567890', '2024-05-22'), "Phone format should be like: +7 000 000 00 00!")
        self.assertEqual(add_order('name', 'text', '+7 123 456 78 90', '2024-05-22'), None)

    def test_date_validation(self):
        # �������� ���� �� ��, ��� ��� �� ������ ������� ����
        self.assertEqual(add_order('name', 'text', '+7 000 000 00 00', '2022-05-22'), "Date should not be greater than today!")
        self.assertEqual(add_order('name', 'text', '+7 000 000 00 00', '2024-05-22'), None)