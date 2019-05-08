import csv
import os
import queue as q
from parser import Parser

from consolewriter import ConsoleWriter
from logmonitor import LogMonitor
from logproducer import LogProducer
from windows.stats import Stats
from windows.traffic_alerts import TrafficAlerts

DEFAULT_STATS_WINDOW = 10

DEFAULT_ALERT_WINDOW = 120

BUFFER_SIZE = 10


def main():
    appParser = Parser.build_log_parser()
    args = appParser.parse_args()

    fileDir = os.path.dirname(os.path.realpath('__file__'))
    fileLocation = '../' + args.FileName
    fileName = os.path.join(fileDir, fileLocation)

    reader = csv.reader(open(fileName, newline=''))
    next(reader)

    log_q = q.PriorityQueue(BUFFER_SIZE)
    log_producer = LogProducer(log_q, reader)

    display = ConsoleWriter()

    alert_window_interval = args.interval if args.alert_interval else DEFAULT_ALERT_WINDOW
    alert_window = TrafficAlerts(alert_window_interval, display)

    stats_window_interval = args.interval if args.stats_interval else DEFAULT_STATS_WINDOW
    stats_window = Stats(stats_window_interval, display)

    monitor = LogMonitor(log_q, alert_window, stats_window)

    display.start()
    log_producer.start()
    monitor.start()


if __name__ == "__main__":
    main()
