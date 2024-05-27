from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('./0524/csv/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)
dates, prcps=[],[]
for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prcp = float(row[5])
    except ValueError :
        print(f'Missing data = {row[5]}')
    else :
        prcps.append(prcp)
        dates.append(current_date)
print(prcps)
print(header_row)

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color = 'red')

ax.set_title("Daily PRCP", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('precipitation(mm)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()