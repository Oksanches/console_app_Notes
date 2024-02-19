import os


def load():
    data = read_file()
    data = data.split('\n')
    for i in data:
        notes = i.split('&')
        container_notes.append(notes)


def save():
    write_data = []
    for i in container_notes:
        notes = '&'.join(i)
        write_data.append(notes)
    write_data = '\n'.join(write_data)
    with open(path, 'w') as file: file.write(write_data)


def read_file():
    with (open(path, 'r') as file):
        return file.read()


def create_path() -> str:
    """
    Проверяет на наличие дирректории для хранения каталога заметок.
    В случаи отсутствия - создает
    :return: string (path)
    """
    path = os.environ.get('LOCALAPPDATA')
    path = path + '\\Notes_App'
    if not os.path.isdir(path):
        os.mkdir(path)
        return create_path()
    path = path + '\\notes_user.oks'
    if not os.path.isfile(path):
        file = open(path, 'w')
        file.close()
        return create_path()
    return path


container_notes = []


path = create_path()


diction_menu = {'main': ['add', 'view', 'open', 'del', 'edit', 'search', 'convert'],
                'prior': ['1', '2', 'undo'],
                'edit': ['name', 'disc', 'prior']}


diction_com = {'add': 'Создать заметку',
               'open': 'Просмотреть заметку',
               'search': 'Найти заметку',
               'view': 'Вывести имена заметок',
               'edit': 'Редактировать заметку',
               'del': 'Удалить заметку',
               'convert': 'Конвертировать в CSV',
               'y': '',
               'n': '',
               'info': '',
               'stop': '',
               '1': 'Обычная заметка',
               '2': 'Важная заметка',
               'undo': 'Отменить команду',
               'name': 'Наименование заметки',
               'disc': 'Содержание заметки',
               'prior': 'Важность'}



