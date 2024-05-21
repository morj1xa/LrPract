from asyncio.windows_events import NULL
from bottle import Bottle, post, request, template
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
            # Получаем абсолютный путь к текущему каталогу
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Создаем абсолютный путь к файлу JSON в текущем каталоге
            json_file = os.path.join(current_dir, 'json_data.json')

            # Проверяем, существует ли файл JSON, если нет - создаем его
            if not os.path.exists(json_file):
                with open(json_file, 'w') as new_json:
                    new_json.write('{}')

            # Открываем файл JSON и загружаем его содержимое
            with open(json_file, 'r') as read_json:
                questions = json.load(read_json)

            # Добавляем новый вопрос и почту в словарь
            if mail in questions:
                questions[mail].append(quest) 
            else:
                questions[mail] = [quest]

            # Записываем обновленные данные в файл JSON
            with open(json_file, 'w') as write_json:
                json.dump(questions, write_json)
        
            return "Thanks, "+username+"! The answer will be sent to the mail %s" % mail + f" |  Access Date: {curdate}"
        else:
            return "Dear, "+username+"! You have entered an incorrect email!"
    

def mailCheck(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

orders = []

@post('/orders', method='POST')
def show_orders():
    # Здесь вы можете добавить логику загрузки данных из файла, если это необходимо
    # Пример:
    # with open('orders.txt', 'r') as file:
    #     orders = file.readlines()
    orders = []  # Заглушка для списка заказов
    return template('layout', title='Placed orders', orders=orders)

# Обработчик POST-запроса для добавления нового заказа
@post('/add_order', method='POST')
def add_order():
    name = request.forms.get('name')
    text = request.forms.get('text')
    phone = request.forms.get('phone')
    date = request.forms.get('date')
    
    # Создание словаря с данными нового заказа
    new_order = {'name': name, 'text': text, 'phone': phone, 'date': date}
    
    # Добавление нового заказа в список заказов
    orders.append(new_order)
    
    with open('orders.txt', 'a') as file:
        file.write(f"{name}, {text}, {phone}, {date}\n")
        
    # После записи данных в файл, обычно выполняется перенаправление на другую страницу или обновление текущей
    return "Order added successfully!"

if __name__ == '__main__':
    app.run(debug=True)