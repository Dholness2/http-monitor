import argparse
from collections import namedtuple

APP_DESCRIPTION = "Monitor log stats based on provided  intervals from supplied csv file"


class Parser:

    @staticmethod
    def build_log_parser():
        AppArgs = namedtuple('Args', 'arg type help_description')
        log_monitor_args = [AppArgs('FileName', str, 'Provide file name of csv logs'),
                            AppArgs('--AlertInterval', int, 'provide alert interval in seconds ex. 10 would equal 10s')]
        return Parser._create_parser(log_monitor_args)

    @staticmethod
    def _create_parser(log_monitor_args):
        parser = argparse.ArgumentParser(description=APP_DESCRIPTION)
        for arg in log_monitor_args:
            parser.add_argument(arg.arg, help=arg.help_description, type=arg.type)
        return parser
