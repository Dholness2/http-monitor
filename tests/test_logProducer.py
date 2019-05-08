from collections import namedtuple
from queue import PriorityQueue

from src.logproducer import LogProducer


def test_run_appends_rows_to_q_as_log():
    Log = namedtuple('Log', 'date logList')
    reader = [["10.0.0.4", "-", "apache", 1549573860, "GET /api/user HTTP/1.0", 200, 1234]]
    test_q = PriorityQueue()
    test_producer = LogProducer(test_q, reader)

    test_producer.run()

    assert Log(1549573860, reader[0]) == test_q.get()
