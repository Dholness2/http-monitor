from collections import namedtuple
from unittest.mock import Mock

from src.windows.stats import Stats
from .resources.logfactory import LogFactory

Log = namedtuple('Log', 'date logList')

factory = LogFactory()

Log = namedtuple('Log', 'date logList')


def test_put_log_publishes_stats_after_threshold_is_passed():
    expected_response = '200     GET /api/user HTTP/1.0'

    test_processor_mock = Mock()
    test_display_mock = Mock()
    test_processor_mock.build_log_stats.return_value = expected_response
    test_interval = 3  # in seconds
    test_window = Stats(test_interval, test_processor_mock, test_display_mock)
    factory.build_base_log_windows(test_window)

    window_trigger_stamp = 1549573860 + 4
    trigger_item = factory.create_trigger_log(window_trigger_stamp)
    test_window.put_log(trigger_item)

    test_display_mock.print_titled_values.assert_called_with(expected_response)


def test_put_log_does_not_publish_when_threshold_is_not_passed():
    expected_response = '200     GET /api/user HTTP/1.0'

    test_processor_mock = Mock()
    test_display_mock = Mock()
    test_processor_mock.build_log_stats.return_value = expected_response
    test_interval = 5  # in seconds
    test_window = Stats(test_interval, test_processor_mock, test_display_mock)
    factory.build_base_log_windows(test_window)

    window_trigger_stamp = 1549573860 + 4
    trigger_item = factory.create_trigger_log(window_trigger_stamp)
    test_window.put_log(trigger_item)

    test_display_mock.print.assert_not_called()
