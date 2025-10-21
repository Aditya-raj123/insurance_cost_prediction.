import logging
import os
from datetime import datetime


#directory where logs will be stored
#print(os.path.join(os.getcwd(), 'logs'))   
LOGS_DIR = os.path.join(os.getcwd(), 'logs') 
os.makedirs(LOGS_DIR, exist_ok=True)  # Create logs directory if it doesn't exist
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)
#print(f"Log file path: {LOG_FILE_PATH}")

logging.basicConfig(
    filename=os.path.join("logs", "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)