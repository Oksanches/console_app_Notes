def greeting_mess():
    print('Приложение Notes запущено! Добро пожаловать:)')


def print_menu(lst):
    for i in lst:
        print(f'\t{i}')


def input_com():
    return input('->')


def input_data(mess: str):
    print(mess)
    return input('>>')