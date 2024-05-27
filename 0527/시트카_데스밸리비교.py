from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path1 = Path('./0527/csv/sitka_weather_2021_full.csv')
lines1 = path1.read_text().splitlines()
reader1 = csv.reader(lines1)
header_row1 = next(reader1)

path2 = Path('./0527/csv/death_valley_2021_full.csv')
lines2 = path2.read_text().splitlines()
reader2 = csv.reader(lines2)
header_row2 = next(reader2)

dates1, tmps1=[],[]
for row in reader1:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        tmp = int(row[7])
    except ValueError :
        print(f'Missing data = {row[7]}')
    else :
        tmps1.append(tmp)
        dates1.append(current_date)
tmps2=[]
for row in reader2:
    try:
        tmp = int(row[6])
    except ValueError :
        print(f'Missing data = {row[6]}')
    else :
        tmps2.append(tmp)
        
        
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates1, tmps1, color = 'red')
ax2 = ax.twinx()
ax2.plot(dates1, tmps2, color = 'blue')
ax.set_ylim([0, 150])
ax2.set_ylim([0, 150])
ax.fill_between(dates1, tmps1, tmps2, facecolor = 'blue', alpha=0.1)

ax.set_title("Daily Temperature Comprison", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature(F)', fontsize=16)
ax2.set_ylabel('Temperature(F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()