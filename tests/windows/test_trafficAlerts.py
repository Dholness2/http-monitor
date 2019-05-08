from collections import namedtuple
from unittest.mock import Mock

from src.windows.trafficalerts import TrafficAlerts
from .resources.logfactory import LogFactory

Log = namedtuple('Log', 'date logList')

factory = LogFactory()


def test_put_log_publishes_alert_when_threshold_exceeds():
    test_interval = 1
    test_threshold = 1
    test_display_mock = Mock()
    test_window = TrafficAlerts(test_interval, test_display_mock, test_threshold)
    factory.build_base_log_windows(test_window)
    window_trigger_stamp = 1549573860 + 11
    trigger_item = factory.create_trigger_log(window_trigger_stamp)

    expected_result = 'High traffic generated an alert hits=3, triggerd at time2019-02-07T16:11:11 '
    test_window.put_log(trigger_item)

    test_display_mock.print.assert_called_with(expected_result)


def test_put_log_publishes_alert_when_traffic_has_recovered():
    test_interval = 3
    test_threshold = 4
    test_display_mock = Mock()
    test_window = TrafficAlerts(test_interval, test_display_mock, test_threshold)

    window_trigger_stamp = 1549573860 + 4
    factory.build_base_log_windows(test_window)
    trigger_recover_item = factory.create_trigger_log(window_trigger_stamp)
    expected_result = 'Traffic has dropped below average rate at=2019-02-07T16:11:04'

    test_window.recovery_mode = True
    test_window.put_log(trigger_recover_item)

    test_display_mock.print.assert_called_with(expected_result)
