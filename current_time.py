from datetime import datetime

time = datetime.now()

current_time = time.strftime("%H:%M:%S")
print("Current time: ", current_time)