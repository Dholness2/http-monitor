from collections import namedtuple
from queue import PriorityQueue
from unittest.mock import Mock

from src.logmonitor import LogMonitor


def test_run_appends_rows_to_q_as_log():
    Log = namedtuple('Log', 'date logList')
    reader = [["10.0.0.4", "-", "apache", 1549573860, "GET /api/user HTTP/1.0", 200, 1234]]
    test_log = Log(1549573860, reader[0])

    test_q = PriorityQueue()
    test_q.put(test_log)
    mock_window = Mock()
    test_monitor = LogMonitor(test_q, mock_window, mock_window)

    test_monitor.run()

    mock_window.put_log.assert_called_with(test_log)
