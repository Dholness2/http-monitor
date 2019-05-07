import art


class ConsoleWriter(object):

    def start(self):
        art.tprint("HTTP Monitor ", "rnd-xlarge")

    def print(self, vals):
        print(vals)
