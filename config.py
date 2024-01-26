import os


def load():
    data = read_file()
    data = '\n'.split(data)
    for i in data:
        notes = '&'.split(i)
        container_notes.append(notes)


def save():
    write_data = []
    for i in container_notes:
        notes = '&'.join(i)
        write_data.append(notes)
    write_data = '\n'.join(write_data)
    with open(path, 'w') as file: file.write(write_data)


def read_file():
    with open(path, 'r') as file:
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


diction_menu = {'main': ['add', 'search', 'view', 'del', 'edit', 'convert', 'sort'],
                'prior': ['1', '2', 'undo']}


diction_com = {'add': 'Создать заметку',
               'search': 'Найти заметку',
               'view': 'Просмотр всех заметок',
               'edit': 'Редактировать заметку',
               'del': 'Удалить заметку',
               'convert': 'Конвертировать',
               'sort': 'Отсортировать по критерию',
               'y': '',
               'n': '',
               'info': '',
               'stop': '',
               '1': 'Обычная заметка',
               '2': 'Важная заметка',
               'undo': 'Отменить команду'}


