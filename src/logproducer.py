from collections import namedtuple
import threading

class LogProducer(threading.Thread):

    def __init__(self, log_iterator_stream, q):
        super(LogProducer, self).__init__()
        self.q = q
        self.log_iterator_stream = log_iterator_stream

    def run(self):
        Log = namedtuple('Log', 'date logList')
        for row in self.log_iterator_stream:
            self.q.put(Log(int(row[3]), row))


