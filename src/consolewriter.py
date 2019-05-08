import art


class ConsoleWriter(object):

    def start(self):
        art.tprint("HTTP Monitor ", "rnd-xlarge")

    def print(self, vals):
        print("------------------------------------\n")
        print(vals)
        print("------------------------------------\n")

    def print_titled_values(self, titled_values):
        for key, val in titled_values.items():
            print(key)
            print("------------------------------------\n")
            print(val + "\n")

