% rebase('layout.tpl', title=title, year=year)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title style="color:white">Placed orders</title>
    <style>
        /* �������� ����� �����, ���� ���������� */
    </style>
</head>
<body>
    <h1 style="color:white">Placed orders</h1>
    <ul id="order-list">
        <!-- �������� ������ ����� ��������� ����������� � ������� Python -->
    </ul>
    <h2 style="color:white">Add a new order:</h2>
    <form action="/add_order" method="post">
        <label style="color:white" for="author">Author:</label><br>
        <input type="text" id="author" name="author" required><br>
        <label style="color:white" for="text">Text (Description):</label><br>
        <textarea id="text" name="text" required></textarea><br>
        <label style="color:white" for="date">Date:</label><br>
        <input type="date" id="date" name="date" required><br>
        <!-- �������������� ����, ����� ��� �������, ����� ���� ��������� ����� -->
        <button type="submit">Post</button>
    </form>
</body>
</html>