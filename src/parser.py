import argparse
from collections import namedtuple
APP_DESCRIPTION = "Monitor log stats based on provided  intervals from supplied csv file"
AppArgs = namedtuple('Args', 'arg type help_description')
LO = [AppArgs('FileName', str, 'Provide file name of csv logs'),
                     AppArgs('--AlertInterval', int, 'provide alert interval in seconds ex. 10 would equal 10s')]
class Parser:

    @staticmethod
    def build_parser():
        parser = argparse.ArgumentParser(description=APP_DESCRIPTION)
        for arg in log_monitior_args:
            parser.add_argument(arg.arg, help=arg.help_description, type=arg.type)
        return parser


