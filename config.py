import os


def load():
    global path
    path = create_path()
    read_file()


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


def read_file():
    file = open(path, 'r')
    data = file.read()
    file.close()
    print(data)


def save():
    pass


path = None


diction_menu = {'main': ['add', 'search', 'view', 'del', 'edit', 'convert', 'sort']}

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
               'stop': ''}


