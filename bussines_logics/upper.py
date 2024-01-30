from bussines_logics.lower import *
from datetime import datetime as dt
from config import container_notes, save


def create_notes(data):
    current_time = f'{dt.now()}'
    date = current_time[:10:]
    data.append(f'{current_time[11:16:]} {date[8:]}.{date[5:7]}.{date[:4]}')
    container_notes.append(data)
    save()
    return f'Заметка {data[0]} успешно создана'


def take_name_notes():
    view_data = []
    for i in range(len(container_notes)):
        view_data.append(f'{i+1}. {container_notes[i][0]}')
    return view_data


def search_notes(key):
    for i in container_notes:
        if key == i[0]:
            return i
    return [False]


def format_notes(notes):
    red = '\033[31m'
    clean = '\033[0m'
    return (f"\t{red if notes[2] == 'Важная' else clean}Имя заметки: {notes[0]}{clean}"
            f"\n\tСодержание: {notes[1]}\n\tДата создания: {notes[3]}")


def check_duplicate(target):
    return False