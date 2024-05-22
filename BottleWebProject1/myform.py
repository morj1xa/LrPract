# -*- coding: utf-8 -*-
from asyncio.windows_events import NULL
from bottle import Bottle, post, redirect, request, template
import re
from datetime import datetime
import pdb
import os
import json

app = Bottle()

@post('/home', method='post')
def my_form():
    quest = request.forms.get('QUEST')
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    #pattern = re.compile(r"^\S+@\S+\.\S+$")
    
    if mail == "" or username == "" or quest == "":
        return "All forms must be filled"
    else:
        if mailCheck(mail):
            curdate = datetime.now()
            # �������� ���������� ���� � �������� ��������
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # ������� ���������� ���� � ����� JSON � ������� ��������
            json_file = os.path.join(current_dir, 'json_data.json')

            # ���������, ���������� �� ���� JSON, ���� ��� - ������� ���
            if not os.path.exists(json_file):
                with open(json_file, 'w') as new_json:
                    new_json.write('{}')

            # ��������� ���� JSON � ��������� ��� ����������
            with open(json_file, 'r') as read_json:
                questions = json.load(read_json)

            # ��������� ����� ������ � ����� � �������
            if mail in questions:
                questions[mail].append(quest) 
            else:
                questions[mail] = [quest]

            # ���������� ����������� ������ � ���� JSON
            with open(json_file, 'w') as write_json:
                json.dump(questions, write_json)
        
            return "Thanks, "+username+"! The answer will be sent to the mail %s" % mail + f" |  Access Date: {curdate}"
        else:
            return "Dear, "+username+"! You have entered an incorrect email!"
    

def mailCheck(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

orders = []


@post('/orders')
def show_orders():
    # ����� �� ������ �������� ������ �������� ������ �� �����, ���� ��� ����������
    # ������:
    with open('orders.txt', 'r') as file:
         orders = file.readlines()
    return template('layout', title='Placed orders', orders=orders)

# ���������� POST-������� ��� ���������� ������ ������
@post('/add_order', method='POST')
def add_order():
    name = request.forms.get('name')
    text = request.forms.get('text')
    phone = request.forms.get('phone')
    date = request.forms.get('date')
    
    error_message = validate_order(name, text, phone, date)
    if error_message:
        return error_message
    
    # �������� ������� � ������� ������ ������
    new_order = {'name': name, 'text': text, 'phone': phone, 'date': date}
    
    # ���������� ������ ������ � ������ �������
    orders.append(new_order)
    
    with open('orders.txt', 'a') as file:
        file.write(f"{name}, {text}, {phone}, {date}\n")
        
    # ����� ������ ������ � ����, ������ ����������� ��������������� �� ������ �������� ��� ���������� �������
    return "Order added successfully!"


def validate_order(name, text, phone, date):
    # �������� ����� �� ���������� ����� � ���������� ����
    if not re.match("^[a-zA-Z]+$", name):
        return "Name should contain only English letters and no digits!"

    # �������� ������ �� ����� �� ����� 3 ��������
    if len(text) < 3:
        return "Text should be at least 3 characters long!"

    # �������� ������� ��������
    if not re.match("^\\+7 \\d{3} \\d{3} \\d{2} \\d{2}$", phone):
        return "Phone format should be like: +7 000 000 00 00!"

    # �������� ���� �� ��, ��� ��� �� ������ ������� ����
    today = datetime.today().strftime('%Y-%m-%d')
    if date > today:
        return "Date should not be greater than today!"

    return None


if __name__ == '__main__':
    app.run(debug=True)