import startpro as dn


def main():
    while True:
        print('Доступный функционал работы с заметками:' + '\n'
              + '1 - Показать, 2 - Найти по дате, 3 - Добавить, 4 - Изменить, 5 - Удалить, 0 - Выйти из приложения' + '\n')
        mode = input('Введите опцию: ')
        if mode == '1':
            dn.show_notes()
        elif mode == '2':
            dn.by_date()
        elif mode == '3':
            dn.add_note()
        elif mode == '4':
            dn.edit_note()
        elif mode == '5':
            dn.delete_note()
        elif mode == '0':
            break
        else:
            print('Такой опции нет, попробуйте еще раз.')

if __name__ == '__main__':
    main()