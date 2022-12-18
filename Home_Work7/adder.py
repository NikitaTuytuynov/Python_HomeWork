import csv


def crate_contact():
    with open('contact.csv', 'a') as file:
        i = 1
        while i <= 100:
            user = [f'Name_{i}', f'Second_name_{i}', f'Number_{i}', f'Description_{i}\n']
            file.write(";".join(user))
            i += 1
        print("Успешно сгенерировано 100 контактов, и внесены в файл contact.csv")
    file.close()


def add_contact():
    with open('contact.csv', 'a') as file:
        user = []
        user.append(input('Введите имя контакта: '))
        user.append(input('Введите фамилию контакта: '))
        user.append(input('Введите телефон контакта: '))
        user.append(input('Введите описание контакта: ') + '\n')
        file.write(";".join(user))
        print("Контакт успешно добавлен.")


def print_contacts():
    with open('contact.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def import_contact():
    data = input('Введите имя файла, без расширения из которого будет осуществляться экспорт контактов, ОБЯЗАТЕЛЬНО ФОРМАТА .txt: ')
    with open(f'{data}.txt', 'r') as file:
        reader = file.read()
        with open('contact.csv', 'a') as file1:
            file1.write(reader)
            print(f'Успешный импорт из файла {data}.txt')


def export_contacts():
    data = input('Введите имя файла: ')
    frmt = input('Укажите формат экспортного файла\n1. .txt\n2. .csv\nСделайте выбор: ')
    design = input('Укажите структуру экспортного файла\n'
                   '1. В файле на одной строке хранится одна часть записи, пустая строка - разделитель\n'
                   '2. файле на одной строке хранится все записи, символ разделитель - ;\nСделайте выбор: ')
    if frmt == '1':
        if design == '1':
            with open('contact.csv', 'r') as file1:
                reader = csv.reader(file1)
                with open(f'{data}.txt', 'a') as file:
                    for row in reader:
                        for el in row:
                            el = el.split(";")
                            file.write("\n".join(el) + '\n' + '\n')
        if design == '2':
            with open('contact.csv', 'r') as file1:
                reader = csv.reader(file1)
                with open(f'{data}.txt', 'a') as file:
                    for row in reader:
                        file.write("".join(row) + '\n')
        print(f'Успешно экспортированно в файл {data}.txt')
    if frmt == '2':
        if design == '1':
            with open('contact.csv', 'r') as file1:
                reader = csv.reader(file1)
                with open(f'{data}.csv', 'a') as file:
                    for row in reader:
                        for el in row:
                            el = el.split(";")
                            file.write("\n".join(el) + '\n' + '\n')
        if design == '2':
            with open('contact.csv', 'r') as file1:
                reader = csv.reader(file1)
                with open(f'{data}.csv', 'a') as file:
                    for row in reader:
                        file.write("".join(row) + '\n')
        print(f'Успешно экспортированно в файл {data}.csv')


def search_contact():
    result = input('Введите ключевое слово или номер: ')
    with open('contact.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            row = str(row)
            if row.count(result) >= 1:
                print(row)


def remove_contact():
    result = input('Введите ключевое слово или номер для поиска контакта на удаление : ')
    a = []
    i = 0
    with open('contact.csv', 'r+') as file:
        reader = csv.reader(file)
        for row in reader:
            row = str(row)
            if row.count(result) >= 1:
                a.append([row, i])
            i += 1
    a = list(enumerate(a))
    for el in a:
        print(f'#{el[0]} - {el[1][0]}')
    d = int(input('Это список совпадений\nВыберете по номеру контакт, который нужно удалить: '))
    e = a[d]
    r = e[1][1]
    with open('contact.csv', 'r+') as file:
        reader = csv.reader(file)
        reader = list(reader)
        reader.pop(r)
        result = "\n".join(map(str, reader))
    with open('contact.csv', 'w') as file:
        file.write(result)
    print('Контакт успешно удалён.')