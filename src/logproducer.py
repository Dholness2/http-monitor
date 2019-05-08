import threading
from collections import namedtuple

DATE_INDEX = 3


class LogProducer(threading.Thread):

    def __init__(self, q, reader):
        super(LogProducer, self).__init__()
        self.reader = reader
        self.q = q

    def run(self):
        Log = namedtuple('Log', 'date logList')
        for row in self.reader:
            self.q.put(Log(int(row[DATE_INDEX]), row))
