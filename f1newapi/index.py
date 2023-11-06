import fastf1

# session = fastf1.get_session(2023, 'Austin', 'Q')
session = fastf1.get_session(2023, 'Austin', 'R')
print(session)
session.load(telemetry=False, laps=False, weather=False)
hamilton = session.get_driver('HAM')
print(hamilton['FirstName'])