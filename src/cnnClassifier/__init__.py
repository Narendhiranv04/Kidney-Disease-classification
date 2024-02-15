import os
import sys
import logging

logging_str = "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"
#it shows the current time at which it runs, log levelname that is, information log
#module - which module we're running this file
#message - to be returned.
 
log_dir="logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath), #I also want to see the file
        logging.StreamHandler(sys.stdout) #prints the log inside the terminal as well
    ]
)

logger = logging.getLogger("cnnClassifierLogger") #Creating a logger object.    