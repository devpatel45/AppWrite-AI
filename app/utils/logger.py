import logging
import os
from logging.handlers import RotatingFileHandler

# Ensure logs directory exists
LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'Logs')
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, 'app.log')

# Create logger
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# Create file handler for logging to file
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=1)
file_handler.setLevel(logging.INFO)

# Create console handler for logging to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter with filename and function name
formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(filename)s:%(funcName)s -> %(message)s'
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Avoid duplicate handlers
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
