from datetime import datetime as dt


def dec_info():
    return f'\033[45;30;3mINFO:{clear()}\t'


def dec_input():
    return f'\033[47;30;3mINPUT:{clear()}\t'


def dec_error():
    return f'\033[41;30;3mERROR:{clear()}\t'


def main_message():
    return f'\033[1;3m'


def clear():
    return f'\033[0m'
