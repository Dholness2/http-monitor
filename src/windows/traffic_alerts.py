import datetime


class TrafficAlerts:

    def __init__(self, interval):
        self.off_set = None
        self.interval = interval
        self.alert_window = [0] * (self.interval + 1)
        self.recovery_mode = False

    def _is_log_date_outside_of_window(self, item):
        return item.date > (self.off_set + self.interval)

    def put_log(self, item):
        if self.off_set is None:
            self.off_set = item.date
        if self._is_log_date_outside_of_window(item):
            self.process(item)
            self.slide_window(item)
        else:
            self.alert_window[item.date - self.off_set] += 1

    def _is_log_rate_above_average(self):
        return sum(self.alert_window) / self.interval > 10

    def _is_below_log_rate(self):
        return not self._is_log_rate_above_average()

    def process(self, item):
        if not self.recovery_mode:
            if self._is_log_rate_above_average():
                total_request_hits_window = sum(self.alert_window)
                time_of_trigger = self._build_time_stamp(item)
                self.recovery_mode = True
                print("High traffic generated an alert hits={0}, triggerd at time{1}".format(total_request_hits_window, time_of_trigger))
            elif self._is_below_log_rate:
                self.recovery_mode = False
                time_of_trigger = self._build_time_stamp(item)
                print("Traffic has dropped below average rate at={0}".format(time_of_trigger))

    def _build_time_stamp(self, item):
        return datetime.datetime.fromtimestamp(item.date).isoformat()

    def slide_window(self, item):
        self.alert_window = [0] * (self.interval + 1)
        self.alert_window[0] += 1
        self.off_set = item.date
