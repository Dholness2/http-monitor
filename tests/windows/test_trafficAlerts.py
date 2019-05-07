import pytest
from unittest.mock import Mock
from collections import namedtuple

from src.windows.traffic_alerts import TrafficAlerts

Log = namedtuple('Log', 'date logList')


def test_items_load():
    unix_time_stamp = 1549573860
    log_a = Log(unix_time_stamp, ["10.0.0.2", "-", "apache", "1549573860", "GET /api/user HTTP/1.0", "200", "1234"])
    log_b = Log(unix_time_stamp, ["10.0.0.2", "-", "apache", "1549573860", "POST /api/user HTTP/1.0", "200", "1234"])
    log_c = Log(unix_time_stamp, ["10.0.0.2", "-", "apache", "1549573860", "GET /api/user HTTP/1.0", "200", "1234"])
    return [log_a, log_b, log_c]


def test_put_log_publishes_alert_when_threshold_exceeds():
    test_interval = 1
    test_threshold = 1
    test_display_mock = Mock()
    test_window = TrafficAlerts(test_interval, test_display_mock , test_threshold)

    _build_base_log_windows(test_window)

    window_trigger_stamp = 1549573860 + 11
    trigger_item = Log(window_trigger_stamp,
                       ["10.0.0.2", "-", "apache", str(window_trigger_stamp), "GET /api/user HTTP/1.0", "200",
                        "1234"])
    expected_result = 'High traffic generated an alert hits=3, triggerd at time2019-02-07T16:11:11 '
    test_window.put_log(trigger_item)

    test_display_mock.print.assert_called_with(expected_result)

def test_put_log_publishes_alert_when_traffic_has_recovered():



def _build_base_log_windows(test_window):
    for log in test_items_load():
        test_window.put_log(log)
