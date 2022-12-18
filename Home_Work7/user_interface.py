import adder as add


def view():
    flag = True
    while flag:
        rez = input('МЕНЮ: \n'
                    '1. Добавление записи\n'
                    '2. Вывод записей на экран\n'
                    '3. Импорт\n'
                    '4. Экспорт\n'
                    '5. Сгенерировать 100 случайных контактов, и добавить их в базу\n'
                    '6. Поиск записи\n'
                    '7. Удаление записи\n'
                    '0. Выход\n'
                    'Выберете действие: ')
        if rez == '0':
            flag = False
        if rez == '1':
            add.add_contact()
        if rez == '2':
            add.print_contacts()
        if rez == '3':
            add.import_contact()
        if rez == '4':
            add.export_contacts()
        if rez == '5':
            add.crate_contact()
        if rez == '6':
            add.search_contact()
        if rez == '7':
            add.remove_contact()
