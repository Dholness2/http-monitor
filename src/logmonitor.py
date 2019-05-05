import threading

class LogMonitor(object):

    def __init__(self,display, stats_proccessor, q, alert_interval=None):
        super(LogMonitor, self).__init__()
        self.q = q
        self.alert_interval = alert_interval
        self.stats_proccessor = stats_proccessor
        self.display = display

