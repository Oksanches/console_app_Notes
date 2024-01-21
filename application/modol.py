from GUI.console_view import *
from bussines_logics.upper import *
import config


def start_message():
    greeting_mess()


def ending_message():
    pass


def output_menu_com(type: str = 'main'):
    lst = config.diction.get(type)
    print_menu(lst)


def check_com(com: str, type: str) -> bool:
    """
    принимает команду и тип меню, возвращает  тру, если команда есть в соответсвующем меню
    :param com: str
    :param type: str
    :return: bool
    """
    com = com.lower().replace(' ','')
    lst = config.diction.get(type)
    if com in lst: return True
    return False


def output_error_mess():
    pass


    


def get_com():
    return input_com()


