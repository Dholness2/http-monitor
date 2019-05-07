import csv
import os
import queue as q
from parser import Parser

from consolewriter import ConsoleWriter
from logmonitor import LogMonitor
from logproducer import LogProducer
from windows.stats import Stats
from windows.traffic_alerts import TrafficAlerts


def main():
    appParser = Parser.build_log_parser()
    args = appParser.parse_args()

    fileDir = os.path.dirname(os.path.realpath('__file__'))
    fileLocation = '../' + args.FileName
    fileName = os.path.join(fileDir, fileLocation)

    reader = csv.reader(open(fileName, newline=''))
    next(reader)

    log_q = q.PriorityQueue(10)
    log_producer = LogProducer(log_q, reader)

    display = ConsoleWriter()
    alert_window = TrafficAlerts(120, display)
    stats_window = Stats(10)
    monitor = LogMonitor(log_q, alert_window, stats_window)

    display.start()
    log_producer.start()
    monitor.start()


if __name__ == "__main__":
    main()
