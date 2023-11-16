import fastf1
import pandas as pd

# need to create venv for tensorflow, tf uses python3.10, not 12
# import tensorflow as tf

# session = fastf1.get_session(2023, 'Austin', 'Q')

# Before we go into all the pit times, we need to go thru and find all the drivers




all_drivers_pits = {}
all_drivers_fastest_laps = {}
session = fastf1.get_session(2023, 'Austin', 'R')
# print(session)
# session.load()


session.load(telemetry=False, laps=True, weather=True)
# print(session)
# print('Drivers')
drivers = session.results['Abbreviation']
# print(drivers)
counter = 0

for d in drivers:
    # print(d)

    outTime = session.laps.pick_driver(d).PitOutTime
    inTime = session.laps.pick_driver(d).PitInTime
    bestLap = session.laps.pick_driver(d).pick_fastest()['LapTime'].total_seconds()

    # not all laps have in time or out time, we going thru all the laps to check
    outTimes = []
    for i in outTime:
        if i is not pd.NaT:
            # print(i)
            outTimes.append(i)

    inTimes = []
    # print('printing out when vers came in to the pits next')
    for i in inTime:
        if i is not pd.NaT:
            # print(i)
            inTimes.append(i)
    

    # print('printing out differences, let us see what happens')
    # print('are the sizes of outtime and intime the same?')
    
    if len(outTimes) != len(inTimes):
        print('size of outtime and intime not the same, so skipping')
        # print(d)
        # print(outTimes)
        # print(inTimes) 
        continue
    total = 0.0
    for i in range(0, len(outTimes)):
        total += (outTimes[i] - inTimes[i]).total_seconds()
    total /= len(outTimes)
    
    # print(total)
    
    all_drivers_pits[d] = total
    all_drivers_fastest_laps[d] = bestLap
    counter+=1
    # print(all_drivers_pits)

# print(all_drivers_pits)

removeNegativeAvgTimes = []
for key, value in all_drivers_pits.items():
    if value < 0.0:
        # print(key)
        # print(value)
        # print(all_drivers_pits[value])
        removeNegativeAvgTimes.append(key)

for remove in removeNegativeAvgTimes:
    all_drivers_pits.pop(remove)
print(all_drivers_pits) 
print('Printing best laps for all')
print(all_drivers_fastest_laps) 
# for i in all_drivers_pits:
    

# print(outTime)
# print('printing out when vers came in to the pits next')
# print(inTime)
# hamilton = session.get_driver('HAM')
# print(hamilton['FirstName'])