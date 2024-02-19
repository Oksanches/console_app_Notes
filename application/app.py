from application.modol import *
from config import load, save


def run_app():
    load()
    start_message()
    main_loop()
    save()
    ending_message()


def main_loop():
    output_menu_com()
    while True:
        com = pars_com(get_com())

        if com == 'stop':
            return

        if com == 'help':
            output_menu_com()
            continue

        if not check_com(com, 'main'):
            output_error_mess()
            continue

        result = run_command(com)

        if result == 'undo':
            output_error_mess()
            continue
        elif result == 'stop':
            return
        elif result == 'None':
            continue
        output_result(result)
