% rebase('layout.tpl', title=title, year=year)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title style="color:white">{{ title }}</title>
    <style>
        /* �������� ����� �����, ���� ���������� */
    </style>
</head>
<body>
    <h1 style="color:white">{{ title }}</h1>
    
    <!-- ����� ��� ���������� ������ ������ -->
    <form action="/add_order" method="post">
        <label style="color:white" for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br>
        <label style="color:white" for="text">Text (Description):</label><br>
        <textarea id="text" name="text" required></textarea><br>
        <label style="color:white" for="phone">Phone:</label><br>
        <input type="text" id="phone" name="phone" required><br>
        <label style="color:white" for="date">Date:</label><br>
        <input type="date" id="date" name="date" required><br>
        <!-- �������������� ����, ����� ��� �������, ����� ���� ��������� ����� -->
        <button type="submit">Post</button>
    </form>
    
    <!-- ������ ���� ������������ ������� -->
    <h2 style="color:white">Order list:</h2>
    
</body>
</html>