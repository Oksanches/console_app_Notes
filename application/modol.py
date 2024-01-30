from GUI.console_view import *
from bussines_logics.upper import *
from datetime import datetime
import config


def start_message():
    greeting_mess()


def ending_message():
    pass


def output_menu_com(type: str = 'main') -> None:
    """

    :param type:
    :return:
    """
    lst = config.diction_menu.get(type)
    menu = []
    for i in range(len(lst)):
        discript = config.diction_com.get(lst[i])
        menu.append(lst[i] + ' - ' + discript)
    print_menu(menu)


def output_info_mess():
    pass


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
            data = take_data(["Введите имя заметки", "Введите содержание"])
            if data[0] == 'undo':
                output_error_mess()
                return 'undo'
            elif data[0] == 'stop':
                return 'stop'
            buff = set_priority()
            if buff == 'undo':
                output_error_mess()
                return 'undo'
            elif buff == 'stop':
                return 'stop'
            data.append(buff)
            return create_notes(data)

        case 'search':
            pass

        case 'view':
            view_data = take_name_notes()
            print_menu(view_data)
            return 'None'

        case 'del':
            pass

        case 'edit':
            pass

        case 'convert':
            pass

        case 'sort':
            pass


def take_data(lst: list) -> list:
    data = []
    count = 0
    while count != len(lst):
        buff = input_data(lst[count])
        if buff == 'undo':
            return ['undo']
        elif buff == 'stop':
            return ['stop']

        if '&' in buff:
            output_error_mess()
            continue
        data.append(buff)
        count += 1
    return data


def set_priority():
    output_info_mess()
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
