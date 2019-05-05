import argparse


class Parser:

    @staticmethod
    def build_parser(args, parser_description):
        parser = argparse.ArgumentParser(description=parser_description)
        for arg in args:
            parser.add_argument(arg.arg, help=arg.help_description, type=arg.type)
        return parser


