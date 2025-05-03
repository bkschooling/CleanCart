from datetime import datetime

def log_event(message: str, filename: str = "user_activity.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode="a") as file:
        file.write(f"[{timestamp}] {message}\n")
