from bussines_logics.lower import *
from datetime import datetime as dt
from config import container_notes, save

red = '\033[31m'
clean = '\033[0m'

def create_notes(data):
    current_time = f'{dt.now()}'
    date = current_time[:10:]
    data.append(f'{current_time[11:16:]} {date[8:]}.{date[5:7]}.{date[:4]}')
    container_notes.append(data)
    save()
    return f'Заметка {data[0]} успешно создана'


def take_name_notes(container: list = container_notes):
    view_data = []
    for i in range(len(container)):
        view_data.append(f'{i+1}. {red if container[i][2]=="Важная" else clean}{container[i][0]}{clean}')
    return view_data


def search_notes(key):
    for i in container_notes:
        if key == i[0]:
            return i
    return [False]


def format_notes(notes):
    return (f"\t{red if notes[2] == 'Важная' else clean}Имя заметки: {notes[0]}{clean}"
            f"\n\t\t\tСодержание: {notes[1]}\n\t\t\tДата создания: {notes[3]}")


def check_duplicate(target):
    for i in container_notes:
        if target in i[0]:
            return True
    return False


def del_notes(target):
   container_notes.remove(target)
   if target in container_notes:
       return "Заметка не удалена... :с"
   save()
   return f"Заметка {target[0]} была удалена"


def edit_notes(target, atribut, new_data):
    index_notes = container_notes.index(target)

    if atribut == 'name':
        target[0] = new_data
    elif atribut == 'disc':
        target[1] = new_data
    elif atribut == 'prior':
        target[2] = new_data

    current_time = f'{dt.now()}'
    date = current_time[:10:]
    target[3] = f'{current_time[11:16:]} {date[8:]}.{date[5:7]}.{date[:4]}'

    container_notes[index_notes] = target

    save()

    return f'Заметка {target[0]} успешно отредактирована!'


def search_for_name(target: str):
    return [container_notes[i] for i in range(len(container_notes)) if target in container_notes[i][0]]


def convert_data(name_file):
    path_desktop = os.environ.get('IDEA_INITIAL_DIRECTORY')

    with open(path_desktop + name_file, 'w', encoding='cp1251') as file:
        for i in container_notes:
            write_data = ';'.join(i) + '\n'
            file.write(write_data)
        return f'Все данные записаны в CSV файл\n\t\tФайл {name_file} находится на рабочем столе.'
