from collections import namedtuple
from unittest import TestCase

from src.windows.traffic_alerts import TrafficAlerts

Log = namedtuple('Log', 'date logList')


def test_items_load():
    unix_time_stamp = 1549573860
    log_a = Log(unix_time_stamp, ["10.0.0.2", "-", "apache", "1549573860", "GET /api/user HTTP/1.0", "200", "1234"])
    log_b = Log(unix_time_stamp, ["10.0.0.2", "-", "apache", "1549573860", "POST /api/user HTTP/1.0", "200", "1234"])
    log_c = Log(unix_time_stamp, ["10.0.0.2", "-", "apache", "1549573860", "GET /api/user HTTP/1.0", "200", "1234"])
    return [log_a, log_b, log_c]


class TestTrafficAlerts(TestCase):

    def test_put_log(self):
        test_interval = 1
        test_threshold = 1
        test_window = TrafficAlerts(test_interval , test_threshold)
        for log in test_items_load():
            test_window.put_log(log)
        window_trigger_stamp = 1549573860 + 11
        trigger_item = Log(window_trigger_stamp,
                           ["10.0.0.2", "-", "apache", str(window_trigger_stamp), "GET /api/user HTTP/1.0", "200",
                            "1234"])

        result = test_window.put_log(trigger_item)

        assert result == ""

    def test__is_log_rate_above_average(self):
        self.fail()

    def test_process(self):
        self.fail()

    def test__build_time_stamp(self):
        self.fail()

    def test_slide_window(self):
        self.fail()
