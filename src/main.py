import os
import csv
import queue as q

from parser import Parser
from consolewriter import ConsoleWriter
from processor import Processor
from logproducer import LogProducer
from logmonitor import LogMonitor
from windows.traffic_alerts import TrafficAlerts
from windows.stats import Stats

appParser = Parser.build_log_parser()
args = appParser.parse_args()

fileDir = os.path.dirname(os.path.realpath('__file__'))
fileLocation = '../' + args.FileName
fileName = os.path.join(fileDir, fileLocation)

reader = csv.reader(open(fileName, newline=''))
next(reader)

log_q = q.PriorityQueue(10)
log_producer = LogProducer(log_q, reader)

alert_window = TrafficAlerts(120)
stats_window = Stats(10)
display = ConsoleWriter()
monitor = LogMonitor(log_q, alert_window, stats_window)

display.start()
log_producer.start()
monitor.start()


