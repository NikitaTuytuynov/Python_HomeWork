import csv
import random


def crate_workers():
    with open('workers.csv', 'a') as file:
        i = 1
        name = ['Nikita', 'Dima', 'Yriy', 'Sergey', 'Anna', 'Oksana', 'Liza', 'Tatyana', 'Alex', 'Yulia', 'Kirill']
        second_name = ['Atkins', 'Mendoza', 'Smith', 'Sanders', 'Flores',
                       'Abbott', 'Peterson', 'Hines', 'Bailey', 'Kelly']
        pre = ['29', '44', '25']
        job_title = ['developer', 'cleaner', 'manager', 'economist', 'accountant', 'tester', 'team lead']
        while i <= 100:
            user = [random.choice(name), random.choice(second_name),
                    f'+375({random.choice(pre)}){random.randint(1000000, 9999999)}',
                    random.choice(job_title), f'{random.randint(600, 9000)}$',
                    f'{random.randint(1, 10)}years\n']
            file.write(";".join(user))
            i += 1
        print("Успешно сгенерировано 100 работников, и внесены в файл workers.csv")


def add_worker():
    with open('workers.csv', 'a') as file:
        user = []
        user.append(input('Введите имя работника: '))
        user.append(input('Введите фамилию работника: '))
        user.append(input('Введите телефон работника: '))
        user.append(input('Введите должность работника: '))
        user.append(input('Введите зарплату работника работника: ') + '$')
        user.append(input('Введите стаж работника: ') + 'years' + '\n')
        file.write(";".join(user))
        print("Работник успешно добавлен.")


def print_workers():
    with open('workers.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def export_workers():
    data = input('Введите имя файла: ')
    frmt = input('Укажите формат экспортного файла\n1. .txt\n2. .csv\nСделайте выбор: ')
    design = input('Укажите структуру экспортного файла\n'
                   '1. В файле на одной строке хранится одна часть записи, пустая строка - разделитель\n'
                   '2. файле на одной строке хранится все записи, символ разделитель - ;\nСделайте выбор: ')
    if frmt == '1':
        if design == '1':
            with open('workers.csv', 'r') as file1:
                reader = csv.reader(file1)
                with open(f'{data}.txt', 'a') as file:
                    for row in reader:
                        for el in row:
                            el = el.split(";")
                            file.write("\n".join(el) + '\n' + '\n')
        if design == '2':
            with open('workers.csv', 'r') as file1:
                reader = csv.reader(file1)
                with open(f'{data}.txt', 'a') as file:
                    for row in reader:
                        file.write("".join(row) + '\n')
        print(f'Успешно экспортированно в файл {data}.txt')
    if frmt == '2':
        if design == '1':
            with open('workers.csv', 'r') as file1:
                reader = csv.reader(file1)
                with open(f'{data}.csv', 'a') as file:
                    for row in reader:
                        for el in row:
                            el = el.split(";")
                            file.write("\n".join(el) + '\n' + '\n')
        if design == '2':
            with open('workers.csv', 'r') as file1:
                reader = csv.reader(file1)
                with open(f'{data}.csv', 'a') as file:
                    for row in reader:
                        file.write("".join(row) + '\n')
        print(f'Успешно экспортированно в файл {data}.csv')


def search_worker():
    res = input('По какому критерию будет поиск?\n'
                '1. Имени\n'
                '2. Фамилии\n'
                '3. Должность\n'
                '4. Номеру телефона\n'
                '5. Зарплате\n'
                '6. Стажу\n'
                'Сделайте выбор: ')
    result = None
    if res == '1':
        result = input('Введите имя: ')
    if res == '2':
        result = input('Введите фамилию: ')
    if res == '3':
        result = input('Введите должность: ')
    if res == '4':
        result = input('Введите номер телефона: ')
    if res == '5':
        result = input('Введите зарплату работника: ') + '$'
    if res == '6':
        result = input('Ввежите стаж работника: ') + 'years'
    with open('workers.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            row = str(row)
            if row.count(result) >= 1:
                row = row.replace(";", ', ')
                row = row.translate({ord(i): None for i in "[]'"})
                print(row)


def remove_worker():
    result = input('Введите ключевое слово или номер для поиска рабочего на удаление из базы: ')
    a = []
    i = 0
    with open('workers.csv', 'r+') as file:
        reader = csv.reader(file)
        for row in reader:
            row = str(row)
            if row.count(result) >= 1:
                a.append([row, i])
            i += 1
    a = list(enumerate(a))
    for el in a:
        print(f'#{el[0]} - {el[1][0]}')
    d = int(input('Это список совпадений\nВыберете по номеру рабочего, которого нужно удалить: '))
    e = a[d]
    r = e[1][1]
    with open('workers.csv', 'r+') as file:
        reader = csv.reader(file)
        reader = list(reader)
        reader.pop(r)
        result = "\n".join(map(str, reader))
    with open('workers.csv', 'w') as file:
        file.write(result)
    print('Рабочий успешно удалён.')


def sort_workers():
    res = input('По какому критерию будет поиск?\n'
                '1. Имени или фамилии\n'
                '2. Должность\n'
                '3. Номеру телефона\n'
                '4. Зарплате\n'
                '5. Стажу\n'
                'Сделайте выбор: ')
    if res == '1':
        result = input('Введите имя\фамилию: ')
        with open('workers.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row = str(row)
                if row.count(result) >= 1:
                    row = row.replace(';', ',  ')
                    row = row.replace("'", '')
                    row = row.translate({ord(i): None for i in '[]"'})
                    print(row)
        print(f'Это все {result} работающие в компании')
    if res == '2':
        res_dolj = input('По какому критерию будет поиск?\n'
                    '1. Вывести бухгалтерский отдел\n'
                    '2. Вывести разработчиков\n'
                    '3. Вывести тестировщиков\n'
                    '4. Вывести уборщиков\n'
                    '5. Вывести тим лидов\n'
                    '6. Вывести экономистов\n'
                    '7. Вывести менеджеров\n'
                    'Сделайте выбор: ')
        if res_dolj == '1':
            result = 'accountant'
        if res_dolj == '2':
            result = 'developer'
        if res_dolj == '3':
            result = 'tester'
        if res_dolj == '4':
            result = 'cleaner'
        if res_dolj == '5':
            result = 'team lead'
        if res_dolj == '6':
            result = 'economist'
        if res_dolj == '7':
            result = 'manager'
        with open('workers.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row = str(row)
                if row.count(result) >= 1:
                    row = row.replace(';', ', ')
                    row = row.replace("'", '')
                    row = row.translate({ord(i): None for i in '[]"'})
                    print(row)
        print(f'Это все {result} работающие в компании.')
    if res == '3':
        result = input('Введите телефон(без кода): ')
        with open('workers.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row = str(row)
                if row.count(result) >= 1:
                    row = row.replace(';', ', ')
                    row = row.replace("'", '')
                    row = row.translate({ord(i): None for i in '[]"'})
                    print(row)
        print(f'Это все совпадения.')
    if res == '4':
        res_solary = input('По какому критерию будет поиск?\n'
                         '1. <1000$\n'
                         '2. 1000$ - 3000$\n'
                         '3. 3000$ - 5000$\n'
                         '4. 5000$ - 7000$\n'
                         '5. 7000$+\n'
                         '6. Ввести точную сумму\n'
                         'Сделайте выбор: ')
        if res_solary == '1':
            with open('workers.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = str(row)
                    row = row.split(';')
                    row[4] = int(row[4].replace("$", ''))
                    if row[4] < 1000:
                        row[4] = str(row[4]) + '$'
                        row = str(row)
                        row = row.replace("'", '')
                        row = row.translate({ord(i): None for i in '[\]"'})
                        print(row)
        if res_solary == '2':
            with open('workers.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = str(row)
                    row = row.split(';')
                    row[4] = int(row[4].replace("$", ''))
                    if (row[4] > 1000 and row[4] < 3000):
                        row[4] = str(row[4]) + '$'
                        row = str(row)
                        row = row.replace("'", '')
                        row = row.translate({ord(i): None for i in '[\]"'})
                        print(row)
        if res_solary == '3':
            with open('workers.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = str(row)
                    row = row.split(';')
                    row[4] = int(row[4].replace("$", ''))
                    if (row[4] > 3000 and row[4] < 5000):
                        row[4] = str(row[4]) + '$'
                        row = str(row)
                        row = row.replace("'", '')
                        row = row.translate({ord(i): None for i in '[\]"'})
                        print(row)
        if res_solary == '4':
            with open('workers.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = str(row)
                    row = row.split(';')
                    row[4] = int(row[4].replace("$", ''))
                    if (row[4] > 5000 and row[4] < 7000):
                        row[4] = str(row[4]) + '$'
                        row = str(row)
                        row = row.replace("'", '')
                        row = row.translate({ord(i): None for i in '[\]"'})
                        print(row)
        if res_solary == '5':
            with open('workers.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = str(row)
                    row = row.split(';')
                    row[4] = int(row[4].replace("$", ''))
                    if (row[4] > 7000):
                        row[4] = str(row[4]) + '$'
                        row = str(row)
                        row = row.replace("'", '')
                        row = row.translate({ord(i): None for i in '[\]"'})
                        print(row)
        if res_solary == '6':
            result = int(input('Введите точную сумму зарплаты: '))
            with open('workers.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = str(row)
                    row = row.split(';')
                    row[4] = int(row[4].replace("$", ''))
                    if row[4] == result:
                        row[4] = str(row[4]) + '$'
                        row = str(row)
                        row = row.replace("'", '')
                        row = row.translate({ord(i): None for i in '[\]"'})
                        print(row)
    if res == '5':
        res_ex = input('По какому критерию будет поиск?\n'
                           '1. От 1 до 3 лет.\n'
                           '2. От 3 до 5 лет.\n'
                           '3. Более 5 лет\n'
                           'Сделайте выбор: ')
        if res_ex == '1':
            with open('workers.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = str(row)
                    row = row.split(';')
                    row[5] = int(row[5].replace("years']", ''))
                    if row[5] >= 1 and row[5] <= 3:
                        row[5] = str(row[5]) + ' years'
                        row = str(row)
                        row = row.replace("'", '')
                        row = row.translate({ord(i): None for i in '[\]"'})
                        print(row)
        if res_ex == '2':
            with open('workers.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = str(row)
                    row = row.split(';')
                    row[5] = int(row[5].replace("years']", ''))
                    if row[5] >= 3 and row[5] <= 5:
                        row[5] = str(row[5]) + ' years'
                        row = str(row)
                        row = row.replace("'", '')
                        row = row.translate({ord(i): None for i in '[\]"'})
                        print(row)
        if res_ex == '3':
            with open('workers.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = str(row)
                    row = row.split(';')
                    row[5] = int(row[5].replace("years']", ''))
                    if row[5] > 5:
                        row[5] = str(row[5]) + ' years'
                        row = str(row)
                        row = row.replace("'", '')
                        row = row.translate({ord(i): None for i in '[\]"'})
                        print(row)
