from GUI.console_view import *
from bussines_logics.upper import *
from datetime import datetime
import config


def start_message():
    greeting_mess()


def ending_message():
    exit_mess()


def output_menu_com(type_menu: str = 'main') -> None:
    """

    :param type_menu:
    :return:
    """
    lst = config.diction_menu.get(type_menu)
    menu = []
    for i in range(len(lst)):
        discript = config.diction_com.get(lst[i])
        menu.append(lst[i] + ' - ' + discript)
    print_menu(menu)


def output_info_mess(mess):
    print_info_mess(mess)


def output_error_mess(message):
    print_error_mess(message)


def output_result(result):
    print_info_mess(result)


def get_com():
    return input_com()


def pars_com(com: str) -> str:
    """
    Приводит к нижнему регистру строку и убирает пробелы
    :param com: string
    :return: string
    """
    return com.lower().replace(' ', '')


def check_com(com: str, type: str) -> bool:
    """
    принимает команду и тип меню, возвращает  тру, если команда есть в соответсвующем меню
    :param com: str
    :param type: str
    :return: bool
    """
    lst = config.diction_menu.get(type)
    return True if com in lst else False


def run_command(com):
    match com:
        case 'add':
            data = []
            while not data:
                name_notes = take_data("Введите имя заметки")
                if name_notes == 'undo':
                    output_error_mess('Действие отменено пользователем')
                    return 'undo'
                elif name_notes == 'stop':
                    return 'stop'
                elif name_notes == '':
                    output_error_mess("Имя заметки не может быть пустым... Повторите ввод")
                    continue
                elif name_notes == ' ':
                    output_error_mess("Имя заметки не может быть пустым... Повторите ввод")
                    continue
                elif check_duplicate(name_notes):
                    output_error_mess("Заметка с таким именем уже сущевствует\n\t\tПовторите ввод")
                    continue
                data.append(name_notes)
            while True:
                descript = take_data("Введите содержание")
                if descript == 'undo':
                    output_error_mess('Действие отменено пользователем')
                    return 'undo'
                if descript == '':
                    output_error_mess('Содержание не может быть пустым, повторите попытку...')
                    continue
                if descript == ' ':
                    output_error_mess('Содержание не может содержать просто пробел, попробуйте еще раз!')
                    continue
                if descript == 'stop':
                    return 'stop'
                data.append(descript)
                buff = set_priority()
                if buff == 'undo':
                    output_error_mess('Действие отменено пользователем')
                    return 'undo'
                elif buff == 'stop':
                    return 'stop'
                data.append(buff)
                return create_notes(data)

        case 'open':
            name_notes = take_data('Введите имя заметки')
            if name_notes == 'undo':
                output_error_mess('Действие отменено пользователем')
                return 'undo'
            elif name_notes == 'stop':
                return 'stop'
            elif name_notes == ' ':
                output_error_mess('Такой заметки не существует, повторите ввод...')
                return 'None'
                take_data('Введите имя')


            notes = search_notes(name_notes)
            if not notes[0]:
                output_error_mess('Заметка с таким именем не найдена, действие отменено.')
                return 'None'
            return format_notes(notes)

        case 'search':
            target = take_data('Введите часть имени заметки')
            if target == 'undo':
                output_error_mess('Действие отменено пользователем')
                return 'undo'
            elif target == 'stop':
                return 'stop'

            notes_container = search_for_name(target)

            if not notes_container:
                output_error_mess("Не найдено совпадений...")
                return "None"

            container = take_name_notes(notes_container)

            print_menu(container)

            return 'None'

        case 'view':
            view_data = take_name_notes()
            print_menu(view_data)
            return 'None'

        case 'del':
            name_notes = take_data('Введите имя заметки')
            if name_notes == 'undo':
                output_error_mess('Действие отменено пользователем')
                return 'undo'
            elif name_notes == 'stop':
                return 'stop'

            notes = search_notes(name_notes)
            if not notes[0]:
                output_error_mess("Заметка с таким именем не найдена.")
                return 'None'
            return del_notes(notes)

        case 'edit':
            name_notes = take_data('Введите имя заметки')
            if name_notes == 'undo':
                output_error_mess('Действие отменено пользователем')
                return 'undo'
            elif name_notes == 'stop':
                return 'stop'

            notes = search_notes(name_notes)
            if not notes[0]:
                output_error_mess("Заметка с таким именем не найдена.")
                return 'None'

            output_menu_com('edit')

            atribut_notes = None
            while atribut_notes == None:
                atribut = take_data('Какую часть Вы хотите изменить?')
                if atribut == 'undo':
                    output_error_mess('Действие отменено пользователем')
                    return 'undo'
                elif atribut == 'stop':
                    return 'stop'
                atribut_notes = atribut if atribut in ['name', 'disc', 'prior'] else output_error_mess()

            if atribut_notes == 'prior':
                new_data_atribut = set_priority()
            else:
                new_data_atribut = take_data('Введите новое значение')
                if new_data_atribut == 'undo':
                    output_error_mess('Действие отменено пользователем')
                    return 'undo'
                elif new_data_atribut == 'stop':
                    return 'stop'

            return edit_notes(notes, atribut_notes, new_data_atribut)

        case 'convert':
            return convert_data('\\notes.csv')


def take_data(target) -> str:
    while True:
        result = input_data(target)
        if result == 'undo':
            return 'undo'
        elif result == 'stop':
            return 'stop'
        elif result == '':
            return ''
        elif result == ' ':
            return ' '

        if '&' in result:
            output_error_mess('Нельзя использовать символ "&"')
            continue
        return result


def set_priority():
    output_info_mess('Выберите приоритетность для вашей заметки:')
    while True:
        output_menu_com('prior')
        com = input_com()
        if com == '1':
            return 'Обычная'
        elif com == '2':
            return 'Важная'
        elif com == 'undo':
            return 'undo'
        elif com == 'stop':
            return 'stop'
        else:
            output_error_mess("Не верный ввод, выберите цифру из меню:")
