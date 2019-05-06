import pandas as pd

class Stats:

    def __init__(self, interval):
        self.off_set = None
        self.interval = interval
        self.current_window = []

    def put_log(self, item):
        if self.off_set is None:
            self.off_set = item.date
        if item.date > (self.off_set + self.interval):
            self.process(item)
            self.slide_window(item)
        else:
            self.current_window.append(item.logList)

    def process(self, item):
      #  print(str(item.date) + ">" + str((self.off_set + self.interval)))
        df = pd.DataFrame(self.current_window, columns=["remotehost","rfc931","authuser","date","request","status","bytes"])

        # print(df.groupby('request')['request'].count())

       #print(df.groupby('request')[["bytes", "date", "status"]].sum())
       # print(self.current_window)

    def slide_window(self, item):
        self.current_window = []
        self.current_window.append(item.logList)
        self.off_set = item.date
