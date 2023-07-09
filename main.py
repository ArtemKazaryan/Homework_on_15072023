
# Домашняя работа на 15.07.2023 (альтернативные команды закомментированны)

# Создайте некоторую базу данных, используя sqlite3.
# В ней реализуйте 2-3 таблицы, при создании которых используйте различные ограничения и типы данных столбцов.
# После этого наполните таблицу разными данными, используя разные варианты(например, введенные данные вручную,
# данные из какого-то файла и т.д.)
# Также, не забудьте открыть эту базу данных в SQLiteStudio и проверить все свойства.
# После чего попробуйте написать несколько запросов, использующих связи между таблицами.

# Решение:
import sqlite3 as sq

# Мы можем обойтись без функций con.commit() и con.close(), т.к. мы работаем в контекстном режиме

with sq.connect('customers_foods_buy.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS foods(
                   food_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   price INTEGER CHECK(price>0)
                   )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS customers(
                       customers_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       surname TEXT NOT NULL,
                       name TEXT NOT NULL,
                       patronymic TEXT NOT NULL,
                       age INTEGER CHECK(age>0)
                       )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS foods_buy(
                   customers_id INTEGER,
                   food_id INTEGER,
                   coli4 INTEGER CHECK(coli4>=0),
                   CONSTRAINT foods_buy FOREIGN KEY (food_id)
                   REFERENCES foods(food_id)
                   ON DELETE CASCADE
                   ON UPDATE CASCADE,
                   CONSTRAINT foods_buy FOREIGN KEY (customers_id)
                   REFERENCES customers(customers_id)
                   ON DELETE CASCADE
                   ON UPDATE CASCADE
               )''')

    # Можем использовать много раз одинаковые команды с вводом разных данных в ячейки таблицы базы данных foods
    # cur.execute('''INSERT INTO foods VALUES(NULL, "Tomato", 110)''')
    # cur.execute('''INSERT INTO foods VALUES(NULL, "Сucumber", 80)''')
    # cur.execute('''INSERT INTO foods VALUES(NULL, "Onion", 40)''')
    # cur.execute('''INSERT INTO foods VALUES(NULL, "Barbecue", 700)''')
    # cur.execute('''INSERT INTO foods VALUES(NULL, "Ketchup", 80)''')
    # cur.execute('''INSERT INTO foods VALUES(NULL, "Mayonnaise", 140)''')

    # Можем использовать много раз одинаковые команды с вводом разных данных в ячейки таблицы базы данных customers
    # cur.execute('''INSERT INTO customers VALUES(NULL, "Родионова", "Анна", "Васильевна", 25)''')
    # cur.execute('''INSERT INTO customers VALUES(NULL, "Иванов", "Иван", "Иванович", 35)''')
    # cur.execute('''INSERT INTO customers VALUES(NULL, Сидорова, "Ольга", "Петровна', 30)''')
    # cur.execute('''INSERT INTO customers VALUES(NULL, Агафонов, "Борис", "Витальевич", 32)''')
    # cur.execute('''INSERT INTO customers VALUES(NULL, Ефремова, "Глафира", "Рудольфовна", 40)''')
    # cur.execute('''INSERT INTO customers VALUES(NULL, "Петров", "Пётр", "Петрович", 45)''')

    # Можем использовать много раз одинаковые команды с вводом разных данных в ячейки таблицы базы данных foods_buy
    # cur.execute('''INSERT INTO foods_buy VALUES(2, 3, 5)''')
    # cur.execute('''INSERT INTO foods_buy VALUES(4, 1, 4)''')
    # cur.execute('''INSERT INTO foods_buy VALUES(5, 2, 5)''')
    # cur.execute('''INSERT INTO foods_buy VALUES(2, 5, 2)''')
    # cur.execute('''INSERT INTO foods_buy VALUES(2, 1, 9)''')
    # cur.execute('''INSERT INTO foods_buy VALUES(1, 3, 1)''')

    print()
    print('Демонстрация преобразования данных из файла foods.txt:')
    # Получаем значения для foods из файла
    with open('foods.txt', 'r', encoding='utf-8') as f:
        dat = f.read()
        data = dat.split(',')
        print(data)  # для наглядности
        interim_lst = []
        foods = []
        for i in range(0, len(data), 2):
            interim_lst.append(data[i])
            interim_lst.append(data[i + 1])
            foods.append(tuple(interim_lst))
            interim_lst = []
        print(foods)  # для наглядности

    print()
    print('Демонстрация преобразования данных из файла customers.txt:')
    # Получаем значения для customers из файла
    with open('customers.txt', 'r', encoding='utf-8') as f:
        dat = f.read()
        data = dat.split(',')
        print(data)  # для наглядности
        interim_lst = []
        customers = []
        for i in range(0, len(data), 4):
            interim_lst.append(data[i])
            interim_lst.append(data[i + 1])
            interim_lst.append(data[i + 2])
            interim_lst.append(data[i + 3])
            customers.append(tuple(interim_lst))
            interim_lst = []
        print(customers)  # для наглядности

    print()
    print('Демонстрация преобразования данных из файла foods_buy.txt:')
    # Получаем значения для customers из файла
    with open('foods_buy.txt', 'r', encoding='utf-8') as f:
        dat = f.read()
        data = dat.split(',')
        print(data)  # для наглядности
        interim_lst = []
        foods_buy = []
        for i in range(0, len(data), 3):
            interim_lst.append(data[i])
            interim_lst.append(data[i + 1])
            interim_lst.append(data[i + 2])
            foods_buy.append(tuple(interim_lst))
            interim_lst = []
        print(foods_buy)  # для наглядности

        print()

    # Или из заранее заданного списка кортежей, используя много одинаковых запросов с помощью executemany()
    # foods = [("Bread", 40),
    #          ("Butter", 100),
    #          ("Sausage", 250),
    #          ("Tea", 150),
    #          ("Sour_cream", 50),
    #          ("Bacon", 300),
    #          ]

    # customers = [("Бородин", "Борис", "Николаевич", 40),
    #          ("Уваров", "Дмитрий", "Константинович", 31),
    #          ("Жданов", "Георгий", "Владимирович", 28),
    #          ("Корягина", "Антонина", "Николаевна", 53),
    #          ("Лопатина", "Лариса", "Петровна", 21),
    #          ]

    # foods_buy = [(2, 3, 3),
    #              (3, 3, 2),
    #              (1, 5, 7),
    #              (5, 1, 6),
    #              (3, 1, 7)
    #          ]

    # Или записать однотипные команды в таблицу базы данных, используя единственную комманду путём её повторения
    # через цикл for как для значений из файла так и для заранее созданного списка.
    for food in foods:
        cur.execute('''INSERT INTO foods VALUES(NULL, ?, ?)''', food)

    for customer in customers:
        cur.execute('''INSERT INTO customers VALUES(NULL, ?, ?, ?, ?)''', customer)

    for food_buy in foods_buy:
        cur.execute('''INSERT INTO foods_buy VALUES(?, ?, ?)''', food_buy)

    # или используя команду для множественного выполнения однотипной команды
    # как для значений из файла так и для заранее созданного списка.
    cur.executemany('''INSERT INTO foods(food_id, name, price) VALUES(NULL, ?, ?)''', foods)
    cur.executemany('''INSERT INTO customers(customers_id, surname, name, patronymic, age) VALUES(NULL, ?, ?, ?, ?)''', customers)
    cur.executemany('''INSERT INTO foods_buy(customers_id, food_id, coli4) VALUES(?, ?, ?)''', foods_buy)

    # Для получения значений ячеек из таблиц базы данных используем
    print()
    print('Запрос содержимого таблицы foods:')
    cur.execute('''SELECT * FROM foods''')
    # с помощью цикла for повторяем одиночное извлечение значений заданное число раз, например, 5
    for i in range(5):
        print(cur.fetchone())
    # и затем выводим извлеченное лимитированное
    print(cur.fetchmany(5))
    # либо максимальное число значений ячеек
    print(cur.fetchall())

    print()
    print('Запрос содержимого таблицы customers:')
    cur.execute('''SELECT * FROM customers''')
    # с помощью цикла for повторяем одиночное извлечение значений заданное число раз, например, 5
    for i in range(5):
        print(cur.fetchone())
    # и затем выводим извлеченное лимитированное
    print(cur.fetchmany(5))
    # либо максимальное число значений ячеек
    print(cur.fetchall())

    print()
    print('Запрос содержимого таблицы foods_buy:')
    cur.execute('''SELECT * FROM foods_buy''')
    # с помощью цикла for повторяем одиночное извлечение значений заданное число раз, например, 5
    for i in range(5):
        print(cur.fetchone())
    # и затем выводим извлеченное лимитированное
    print(cur.fetchmany(5))
    # либо максимальное число значений ячеек
    print(cur.fetchall())

    print()

    # ЗАПРОСЫ СО СВЯЗЯМИ МЕЖДУ ТАБЛИЦАМИ:
    print('ЗАПРОСЫ СО СВЯЗЯМИ МЕЖДУ ТАБЛИЦАМИ:')
    # 1. Запросим ФИО покупателей, которые совершили покупки на суммы более 1000
    cur.execute('''SELECT surname, name, patronymic
                   FROM customers
                   WHERE customers_id IN (
                   SELECT customers_id
                   FROM foods_buy
                   WHERE food_id IN (
                   SELECT food_id 
                   FROM foods
                   WHERE price*coli4 > 1000))
                ''')
    print(f'Результаты первого запроса со связями между таблицами:')
    # либо максимальное число значений ячеек
    print(cur.fetchall())

    print()

    # 2. Запросим названия продуктов, покупаемых покупателями возрастом младше 30
    cur.execute('''SELECT name
                   FROM foods
                   WHERE food_id IN (
                   SELECT food_id
                   FROM foods_buy
                   WHERE customers_id IN (
                   SELECT customers_id 
                   FROM customers
                   WHERE age < 30))
                ''')
    print(f'Результаты второго запроса со связями между таблицами:')
    # либо максимальное число значений ячеек
    print(cur.fetchall())

    print()

    # 3. Запросим общее количество Tea, который купил Бородин
    cur.execute('''SELECT SUM(foods_buy.coli4) Количество
                   FROM foods_buy, customers, foods
                   WHERE foods_buy.customers_id = customers.customers_id 
                   AND foods_buy.food_id = foods.food_id 
                   AND customers.surname = "Бородин" 
                   AND foods.name = 'Tea'
                ''')

    print(f'Результаты третьего запроса со связями между таблицами:')
    # либо максимальное число значений ячеек
    print(cur.fetchall())

    # Массовое выполнение разнотипных запросов без применения цикла for реализуется с помощью executescript
    cur.executescript('''INSERT INTO foods VALUES(NULL, "Tomato", 110);
                         INSERT INTO foods VALUES(NULL, "Onion", 40);
                         INSERT INTO customers VALUES(NULL, 'Грозный', 'Иван', 'Васильевич', 3);
                         INSERT INTO customers VALUES(NULL, 'Долгополова', 'Ирина', 'Викторовна', 36);
                         INSERT INTO foods_buy VALUES(2, 4, 3);
                         INSERT INTO foods_buy VALUES(5, 4, 2);
                         INSERT INTO foods VALUES(NULL, "Сucumber", 80);
                      ''')




# Откат в выполнении ошибочных SQL-запросов реализуется при помощи rollback
# try:
#     cur.executescript('''BEGIN;
#                          CREATE TABLE IF NOT EXISTS expensive_foods(
#                          food_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                          name TEXT NOT NULL,
#                          price INTEGER CHECK(price>0));
#                          UPDATE foods SET price = price + 150;
#                          INSERT INTO expensive_foods
#                          SELECT * FROM foods WHERE price >=150;''')
# except sq.Error as e:
#     print(e)
#     if con:
#         con.rollback()
# else:
#     if con:
#         con.commit()

