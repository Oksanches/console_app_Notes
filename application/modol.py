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


def get_com():
    pass

