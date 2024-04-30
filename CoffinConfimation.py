from datetime import datetime
## Use to verify personal machine

name = "Alex Coffin"
course = "44671 Streaming Data"
# format: year-month-day timestamp
date = 'Timestamp: {:%Y - %b - %d %H:%M:%S}'.format(datetime.now())

print(f"Hello, I am {name} and I am currently taking {course} and its {date}")