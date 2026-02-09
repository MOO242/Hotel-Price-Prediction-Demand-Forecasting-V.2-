import logging
import os
from datetime import datetime

# 1. Generate the folder name based on the current date
current_date = datetime.now().strftime("%Y-%m-%d")
LOG_DIR = os.path.join(os.getcwd(), "logs", current_date)

# 2. Ensure the daily folder exists
os.makedirs(LOG_DIR, exist_ok=True)

# 3. Define the file path inside that folder
LOG_FILE = f"{current_date}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

# 4. Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler(),  # Keeps console output active
    ],
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info(f"Log directory created at: {LOG_DIR}")
    logger.info("Hotel Pricing V2 Logger is live.")
