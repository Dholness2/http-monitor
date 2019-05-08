from collections import namedtuple

Log = namedtuple('Log', 'date logList')


class LogFactory:

    def test_items_load(self):
        unix_time_stamp = 1549573860
        log_a = Log(unix_time_stamp, ["10.0.0.2", "-", "apache", "1549573860", "GET /api/user HTTP/1.0", "200", "1234"])
        log_b = Log(unix_time_stamp,
                    ["10.0.0.2", "-", "apache", "1549573860", "POST /api/user HTTP/1.0", "200", "1234"])
        log_c = Log(unix_time_stamp, ["10.0.0.2", "-", "apache", "1549573860", "GET /api/user HTTP/1.0", "200", "1234"])
        return [log_a, log_b, log_c]

    def build_base_log_windows(self, test_window):
        for log in self.test_items_load():
            test_window.put_log(log)

    def create_trigger_log(self, window_trigger_stamp):
        log = ["10.0.0.2", "-", "apache", str(window_trigger_stamp), "GET /api/user HTTP/1.0", "200",
               "1234"]
        return Log(window_trigger_stamp, log)
