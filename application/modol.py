from GUI.console_view import *
from bussines_logics.upper import *
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
    for i in range(len(lst)):
        discript = config.diction_com.get(lst[i])
        lst[i] = lst[i] + ' - ' + discript
    print_menu(lst)


def output_error_mess():
    pass


def output_result(result):
    pass


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
            pass
        case 'search':
            pass
        case 'view':
            pass
        case 'del':
            pass
        case 'edit':
            pass
        case 'convert':
            pass
        case 'sort':
            pass
        case '':
            pass
        case 'stop':
            pass

