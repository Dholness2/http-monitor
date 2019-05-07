import datetime


class TrafficAlerts:

    def __init__(self, interval, display, threshold=10):
        self.display = display
        self.threshold = threshold
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
            self._process(item)
            self._slide_window(item)
        else:
            self.alert_window[item.date - self.off_set] += 1  # Keeps count of items added in window via interval

    def _is_log_rate_above_average(self):
        return sum(self.alert_window) / self.interval > self.threshold

    def _is_below_log_rate(self):
        return not self._is_log_rate_above_average()

    def _process(self, item):
        if not self.recovery_mode:
            if self._is_log_rate_above_average():
                self._trigger_alert(item)
        elif self._is_below_log_rate:
            self._reset_recovery_mode(item)

    def _trigger_alert(self, item):
        total_request_hits_window = sum(self.alert_window)
        time_of_trigger = self._build_time_stamp(item)
        self.recovery_mode = True
        self._publish_alert(time_of_trigger, total_request_hits_window)

    def _publish_alert(self, time_of_trigger, total_request_hits_window):
        self.display.print(
            "High traffic generated an alert hits={0}, triggerd at time{1} ".format(total_request_hits_window,
                                                                                    time_of_trigger))

    def _reset_recovery_mode(self, item):
        self.recovery_mode = False
        time_of_trigger = self._build_time_stamp(item)
        self.display("Traffic has dropped below average rate at={0}".format(time_of_trigger))

    def _build_time_stamp(self, item):
        return datetime.datetime.fromtimestamp(item.date).isoformat()

    def _slide_window(self, item):
        self.alert_window = [0] * (self.interval + 1)
        self.alert_window[0] = 1
        self.off_set = item.date
