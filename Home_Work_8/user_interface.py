import modyl as add


def view():
    flag = True
    while flag:
        rez = input('МЕНЮ: \n'
                    '1. Добавление записи\n'
                    '2. Вывод всех записей на экран\n'
                    '3. Экспорт\n'
                    '4. Сгенерировать 100 случайных рабочих, и добавить их в базу\n'
                    '5. Поиск записи\n'
                    '6. Удаление записи\n'
                    '7. Сортировка рабочих\n'
                    '0. Выход\n'
                    'Выберете действие: ')
        if rez == '0':
            flag = False
        if rez == '1':
            add.add_worker()
        if rez == '2':
            add.print_workers()
        if rez == '3':
            add.export_workers()
        if rez == '4':
            add.crate_workers()
        if rez == '5':
            add.search_worker()
        if rez == '6':
            add.remove_worker()
        if rez == '7':
            add.sort_workers()

