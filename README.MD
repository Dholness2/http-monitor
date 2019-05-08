Installation
------------

If you\'re on MacOS, you can install Pipenv easily with Homebrew:

    $ brew install pipenv


Otherwise, refer to the [documentation](https://docs.pipenv.org/install/) for instructions.


To Run APP
----------

    $ cd /httpMonitor
    $ pipenv shell
    $ pipenv install
    $ cd src/
    $ python  main.py sample_csv.csv 
 To Run Test
 -------------
   $ pipenv shell
   $ pytest 
   

App Help, Optional Flags
-------------------

    $ python main.py -h
    
    $ usage: main.py [-h] [--AlertInterval ALERTINTERVAL]
               [--StatsInterval STATSINTERVAL]
               FileName

     Monitor log stats based on provided intervals from supplied csv file

     positional arguments:
     FileName              Provide file name of csv logs

     optional arguments:
      -h, --help            show this help message and exit
      --AlertInterval ALERTINTERVAL
                        provide alert interval in seconds ex. 120 would equal
                        120s
     --StatsInterval STATSINTERVAL
                        provide stats interval in seconds ex. 10 would equal
                        10s

Project Overview
-----------------
  For this project to avoid loading the log file in memory, I leverage a buffered approach; reading only one line at a time using a Producer/Consumer design.
The sample csv file contains a small simulation of the type of  latency that we may  see in a real world example. In this example csv, early timestamp logs are read after later times stamp logs at some instances since order is not guaranteed. To resolve this a priority queue is initialized to ensure to some degree, consumers are seeing the earliest log on the queue.
For processing the data Pandas library is used to process statistics on the current window interval’s logs. In this  example we leverage the concept of “Python as Glue” and delegate the heavy aggregations to Padas performant C based libraries for the statistical analysis.
 
To Improve the application logic, I would create a Log object with its own sorting logic, rather than tulpes. This would make the producer and consumers more extensible. For the log monitor I would also take in multiple alert window types. The current application assumes to window types. This would be a simple change since the log monitor doesn’t have any direct depencines on window minus the assumed interface function of “put_log” shared by the two window types.
 
From a scalability standpoint, if we wanted to monitor traffic across multiple application instances we make want to leverage a distributed queue to support streaming of logs.
This would add to resiliency to our application. If the aoo node would shutdown, the latest logs would be on the queue service and not lost in memory.
 
Instead of pandas we could use an even more performant processor like a spark cluster for running the aggregations in Real Time.

  
  
   