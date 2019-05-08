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
    $ pipenv run python main.py sample_csv.csv
 
 To Run Test
 -------------
   $ pipenv shell
   $ pipenv pytest 
   

App Help, Optional Flags
-------------------

    $ pipenv run python main.py -h
    


Project Overview
-----------------
  For this project to avoid loading the log file in memory,
  I leverage a buffered approach reading only one line at a time using a producer/Consumer design.
  
  The file contains a form simulating latency that we would see in a real world exmaple. In this example csv early timestamp logs are read after later times stamp logs at some instances since order is
  not guaranteed. To resolve this I used a Priority queue to ensure to some degree consumers are seeing the earliest log on the queue.
  
  For processing the stats I used the Pandas library to arranges stats on current logs being accessed in the
  
  
   