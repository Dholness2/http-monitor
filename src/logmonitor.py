import threading


class LogMonitor(threading.Thread):

    def __init__(self, q, traffic_alert_window, stats_window):
        super(LogMonitor, self).__init__()
        self.stats_window = stats_window
        self.traffic_alert_window = traffic_alert_window
        self.q = q
        self._stop = False

    def stop(self):
        print("turning off")
        self._stop = True

    def run(self):
        while True:
            if not self.q.empty():
                item = self.q.get()
                self.traffic_alert_window.put_log(item)
                self.stats_window.put_log(item)
            if self._stop:
                break
