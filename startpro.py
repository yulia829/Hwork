import datetime
import csv
from os import path

file = 'Notes.csv'
headline = ['ID', 'Заголовок', 'Текст', 'Дата/время']
notebook = []


def read_file():
    global notebook, file, previous_id, headline
    while True:
        if path.exists(file):
            with open(file, mode='r', encoding='utf-8', newline='') as f:
                reader = csv.reader(f, delimiter=';')
                notebook = [l for l in reader]
            return notebook
        else:
            choice = input('Создаем новый файл? (Да: 1, нет: 2) \n')
            if choice == '1':
                with open(file, mode='w', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f, delimiter=';')
                    writer.writerow(headline)
                id = int(input('Введите ID (индикатор) заметки: '))
                head = input('Введите заголовок: ')
                text = input('Введите текст заметки: ')
                date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                new_note = [str(id), head, text, date]
                add_data(new_note)
                print('Заметка сохранена.')
                break
            elif choice == '2':
                break
            else:
                print('Такой опции нет, попробуйте еще раз.')



def write_file(new_f):
    with open(file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for l in new_f:
            writer.writerow(l)


def add_data(new_d):
    with open(file, mode='a', encoding='utf-8', newline='\n') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(new_d)


def add_note():
    read_file()
    id = int(input('Введите ID (индикатор) заметки: '))
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    head = input('Введите заголовок: ')
    text = input('Введите текст: ')
    adding_note = [str(id), head, text, date]
    add_data(adding_note)
    print('Заметка сохранена.')


def find_id(id):
    read_file()
    index = 0
    for i in range(1, len(notebook)):
        if notebook[i][0] == id: index = i
    return index


def show_notes():
    read_file()
    result = [[line[i] for i in range(3)] for line in notebook]
    print(result)


def find_note():
    read_file()
    search = input('ID заметки для поиска: ')
    if search == '':
        print('Некорректный ввод. Введите еще раз.')
    else:
        result = search(id=search)
        if len(result) == 0:
            print('Не найдено.')
        else:
            print(result)


def by_date():
    read_file()
    search = input('Введите дату создания в формате ГГГГ-ММ-ДД: ')
    search_result = search(date=search)
    if len(search_result) == 0:
        print('Не найдено.')
    else:
        result = [[line[i] for i in range(3)] for line in search_result]
        print(result)


def search(id='', date=''):
    result = []
    for row in notebook:
        if id != '' and row[0] != id: continue
        if date != '' and row[1].find(date): continue
        result.append(row)
    return result

def edit_note():
    id = input('ID заметки для редактирования: ')
    e_id = find_note(id)
    if e_id == 0:
        print('Не найдено.')
    else:
        print(*notebook[e_id], sep='\t')
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        head = input('Введите новый заголовок: ')
        text = input('Введите текст заметки: ')
        notebook[e_id] = [str(id), date, head, text]
        write_file(notebook)
        print(f'Заметка {id} изменена.')


def delete_note():
    id = input('ID заметки для удаления: ')
    d_id = find_id(id)
    if d_id == 0:
        print('Заметка не найдена.')
    else:
        print(*notebook[d_id], sep='\t')
        note_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        notebook[d_id] = [str(id), '', f'<{note_date}>', '']
        write_file(notebook)
        print(f'Заметка {id} удалена.')




