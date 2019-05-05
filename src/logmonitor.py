import threading


class LogMonitor(threading.Thread):

    def __init__(self, q):
        super(LogMonitor, self).__init__()
        self.q = q
        # self.alert_interval = alert_interval
        # self.stats_proccessor = stats_proccessor
        # self.display = display

    def run(self):
        recovery_mode = False
        alert_window = 120
        alert_window = [0] * 120
        culumitive_sum = 1

        interval = 10
        current_window = []
        start_log = self.q.get()
        current_window.append(start_log.logList)
        start_time = start_log.date
        start_time_alert = start_log.date
        while True:
            if not self.q.empty():
                item = self.q.get()

                if item.date > start_time_alert + 120:
                    if not recovery_mode:
                        if sum(alert_window) / 120 > 10:
                            print("ALERT!!!!!")
                            recovery_mode = True
                    elif sum(alert_window) / 120 < 10:
                        print("Revocered from high trafic!!!!!")
                        recovery_mode = False
                    else:
                        start_time_alert = item.date
                        alert_window = [0] * 120
                alert_window[item.date % 120] += 1
                if item.date > (start_time + interval):
                    print(str(item.date) + ">" + str((start_time + interval)))
                    print("widow of last" + str(interval) + "interval")
                    print(current_window)
                    current_window = []
                    current_window.append(item.logList)
                    start_time = item.date
                else:
                    current_window.append(item.logList)

        return
