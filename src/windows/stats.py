class Stats:

    def __init__(self, interval, processor, display):
        self.processor = processor
        self.display = display
        self.off_set = None
        self.interval = interval
        self.current_window = []

    def put_log(self, item):
        if self.off_set is None:
            self.off_set = item.date
        if item.date > (self.off_set + self.interval):
            stats = self.processor.build_log_stats(self.current_window)
            self.display.print_titled_values(stats)
            self._slide_window(item)
        else:
            self.current_window.append(item.logList)

    def _slide_window(self, item):
        self.current_window = []
        self.current_window.append(item.logList)
        self.off_set = item.date
