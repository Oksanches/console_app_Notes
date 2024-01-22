from application.modol import *
import config


def run_app():
    config.load()
    start_message()
    main_loop()
    config.save()
    ending_message()


def main_loop():
    output_menu_com()
    while True:
        com = pars_com(get_com())
        if not check_com(com, 'main'):
            output_error_mess()
            continue


