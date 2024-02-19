from GUI.system_messege import *


def greeting_mess():
    print(f'{main_message()}Приложение Notes запущено! Добро пожаловать:){clear()}\n')


def exit_mess():
    input(f'{main_message()}Завершение работы. Нажмите Enter для закрытия консоли{clear()}')


def print_info_mess(mess):
    print(f"{dec_info()}{mess}")


def print_error_mess(mess: str):
    print(f"{dec_error()}{mess}")


def print_menu(lst):
    for i in lst:
        print(f'\t\t\t{i}')


def input_com():
    return input(f"{dec_input()}")


def input_data(mess: str):
    print(f'{dec_info()}{mess}')
    return input(f'{dec_input()}')