from collections import namedtuple
import threading
import csv

class LogProducer(threading.Thread):

    def __init__(self, q,args):
        super(LogProducer, self).__init__()
        self.args = args
        self.q = q
        # self.log_iterator_stream = log_iterator_stream

    def run(self):
        with open(self.args.FileName, newline='') as f:
            reader = csv.reader(f)
            next(reader)
            Log = namedtuple('Log', 'date logList')
            for row in reader:
                self.q.put(Log(int(row[3]), row))



