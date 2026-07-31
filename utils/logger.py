from datetime import datetime


LOG_FILE = "outputs/activity.log"


def write_log(action):
    now = datetime.now()

    with open(LOG_FILE, "a") as file:
        file.write(
            f"{now.strftime('%Y-%m-%d %H:%M:%S')} | {action}\n"
        )