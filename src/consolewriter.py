import art
from termcolor import cprint


class ConsoleWriter(object):

    def start(self):
        art.tprint("HTTP Monitor ", chr_ignore=True)

    def print_alert(self, vals):
        print("------------------------------------\n")
        # print(vals)
        cprint(vals, 'white', 'on_red')
        print("------------------------------------\n")

    def print_recovery(self, vals):
        print("------------------------------------\n")
        cprint(vals, 'white', 'on_green')
        print("------------------------------------\n")

    def print_titled_values(self, titled_values):
        for key, val in titled_values.items():
            print(key)
            print("------------------------------------\n")
            print(val + "\n")
