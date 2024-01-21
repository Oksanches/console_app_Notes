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
        input_com()

