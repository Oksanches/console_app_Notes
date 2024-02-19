from GUI.console_view import *
from bussines_logics.upper import *
from datetime import datetime
import config


def start_message():
    greeting_mess()


def ending_message():
    pass


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


def output_error_mess():
    pass


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
                    output_error_mess()
                    return 'undo'
                elif name_notes == 'stop':
                    return 'stop'
                elif check_duplicate(name_notes):
                    output_error_mess()
                    continue
                data.append(name_notes)
            descript = take_data("Введите содержание")
            if descript == 'undo':
                output_error_mess()
                return 'undo'
            elif descript == 'stop':
                return 'stop'
            data.append(descript)
            buff = set_priority()
            if buff == 'undo':
                output_error_mess()
                return 'undo'
            elif buff == 'stop':
                return 'stop'
            data.append(buff)
            return create_notes(data)


        case 'open':
            name_notes = take_data('Введите имя заметки')
            if name_notes == 'undo':
                output_error_mess()
                return 'undo'
            elif name_notes == 'stop':
                return 'stop'

            notes = search_notes(name_notes)
            if not notes[0]:
                output_error_mess()
                return 'None'
            return format_notes(notes)

        case 'search':
            pass

        case 'view':
            view_data = take_name_notes()
            print_menu(view_data)
            return 'None'

        case 'del':
            name_notes = take_data('Введите имя заметки')
            if name_notes == 'undo':
                output_error_mess()
                return 'undo'
            elif name_notes == 'stop':
                return 'stop'

            notes = search_notes(name_notes)
            if not notes[0]:
                output_error_mess()
                return 'None'
            return del_notes(notes)

        case 'edit':
            name_notes = take_data('Введите имя заметки')
            if name_notes == 'undo':
                output_error_mess()
                return 'undo'
            elif name_notes == 'stop':
                return 'stop'

            notes = search_notes(name_notes)
            if not notes[0]:
                output_error_mess()
                return 'None'

            #Что изменить и на что изменить
            #вывести в виде меню что изменить и на что изменить, получить команду/результат и обработать
            #вывести сообщение

            return edit_notes(notes)

        case 'convert':
            pass


def take_data(target) -> str:
    while True:
        result = input_data(target)
        if result == 'undo':
            return 'undo'
        elif result == 'stop':
            return 'stop'

        if '&' in result:
            output_error_mess()
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
            output_error_mess()
