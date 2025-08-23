import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

log_dir= 'log'

log_path=os.path.join(from_root(),log_dir)

os.makedirs(log_path,exist_ok=True)


logging.basicConfig(
    filename=os.path.join(log_path,LOG_FILE),
    format="[%(asctime)s]  %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)