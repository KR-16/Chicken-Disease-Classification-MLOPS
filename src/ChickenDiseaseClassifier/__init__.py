import os
import logging
import sys

loggingString = "[%(asctime)s: %(levelname)s:%(module)s:%(message)s]"

logDirectory = "logs"
logFilepath = os.path.join(logDirectory,"runningLogs.log")
os.makedirs(logDirectory,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=loggingString,
    handlers=[
        logging.FileHandler(logFilepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("ChickenDiseaseClassifierLogger")