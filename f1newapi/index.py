import fastf1
import pandas as pd

# session = fastf1.get_session(2023, 'Austin', 'Q')
session = fastf1.get_session(2023, 'Austin', 'R')
# print(session)
session.load(telemetry=False, laps=True, weather=True)
print(session)

verOutTime = session.laps.pick_driver('VER').PitOutTime
verInTime = session.laps.pick_driver('VER').PitInTime

outTimes = []
for i in verOutTime:
    if i is not pd.NaT:
        # print(i)
        outTimes.append(i)

inTimes = []
# print('printing out when vers came in to the pits next')
for i in verInTime:
    if i is not pd.NaT:
        # print(i)
        inTimes.append(i)


# print('printing out differences, let us see what happens')
for i in range(len(outTimes)):
    print(outTimes[i] - inTimes[i])

# print(verOutTime)
# print('printing out when vers came in to the pits next')
# print(verInTime)
# hamilton = session.get_driver('HAM')
# print(hamilton['FirstName'])