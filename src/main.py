import os
import csv
import queue as q

from src.parser import Parser
from src.consolewriter import ConsoleWriter
from src.processor import Processor
from src.logproducer import LogProducer
from src.logmonitor import LogMonitor
from src.windows.traffic_alerts import TrafficAlerts
from src.windows.stats import Stats

appParser = Parser.build_parser()
args = appParser.parse_args()

fileDir = os.path.dirname(os.path.realpath('__file__'))
fileLocation = '../' + args.FileName
filename = os.path.join(fileDir, fileLocation)

reader = csv.reader(open(filename, newline=''))
next(reader)

log_q = q.PriorityQueue(10)
log_producer = LogProducer(log_q, reader)

alert_window = TrafficAlerts(120)
stats_window = Stats(10)
display = ConsoleWriter()
monitor = LogMonitor(log_q, alert_window, stats_window)

log_producer.start()
monitor.start()


