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
