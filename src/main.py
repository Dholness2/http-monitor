from collections import namedtuple
import threading
import queue as Q
import csv

from src.parser import Parser
from src.consolewriter import ConsoleWriter
from src.processor import Processor
from src.logproducer import LogProducer
from src.logmonitor import LogMonitor

APP_DESCRIPTION = "Monitor log stats based on provided  intervals from supplied csv file"
AppArgs = namedtuple('Args', 'arg type help_description')
log_monitior_args = [AppArgs('FileName', str, 'Provide file name of csv logs'),
                     AppArgs('--AlertInterval', int, 'provide alert interval in seconds ex. 10 would equal 10s')]

appParser = Parser.build_parser(log_monitior_args, APP_DESCRIPTION)
args = appParser.parse_args()

display = ConsoleWriter()

stats_proccessor = Processor()
log_q = Q.PriorityQueue(10)


Log = namedtuple('Log', 'date logList')


# from datetime import datetime
# ts = int("1284101485")
#
# # if you encounter a "year is out of range" error the timestamp
# # may be in milliseconds, try `ts /= 1000` in that case
# print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
monitor = LogMonitor(log_q)
log_producer = LogProducer(log_q, args)
log_producer.start()
monitor.start()
# monitor.start()
