import os
from datetime import datetime

LOG_DIR = "outputs"
LOG_FILE = os.path.join(LOG_DIR, "activity.log")


def write_log(action):
    os.makedirs(LOG_DIR, exist_ok=True)

    with open(LOG_FILE, "a") as file:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{now} | {action}\n")