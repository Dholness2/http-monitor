from collections import namedtuple
import threading
import csv

class LogProducer(threading.Thread):

    def __init__(self, q , reader):
        super(LogProducer, self).__init__()
        self.reader = reader
        self.q = q
        # self.log_iterator_stream = log_iterator_stream

    def run(self):
            Log = namedtuple('Log', 'date logList')
            for row in self.reader:
                self.q.put(Log(int(row[3]), row))



