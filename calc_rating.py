
import pandas as pd
from utils import *

data1 = pd.read_csv('match_data_20230826.csv', parse_dates=['date'])
data2 = pd.read_csv('match_data_20241102.csv', parse_dates=['date'])
data3 = pd.read_csv('match_data_20251102.csv', parse_dates=['date'])

# make one unique file
data = pd.concat([data1, data2, data3])
data = data.drop_duplicates()

print(len(data))

data['diff'] = data.home - data.away
print(data.describe())

# sort by date and then calculate elo
data = data.sort_values('date')

# compare the three elo algos and find smallest error

elo1 = {team: 400 for team in data.hometeam.unique()}
elo2 = {team: 400 for team in data.hometeam.unique()}
elo3 = {team: 400 for team in data.hometeam.unique()}

err = np.zeros(4)

for i, row in data.iterrows():
  R_A1, R_B1 = elo1[row.hometeam], elo1[row.awayteam]
  R_A2, R_B2 = elo2[row.hometeam], elo2[row.awayteam]
  R_A3, R_B3 = elo3[row.hometeam], elo3[row.awayteam]
  S_A = 1 * (row['diff'] > 0)
  E_A1 = expect(R_A1, R_B1)
  E_A2 = expect(R_A2, R_B2)
  E_A3 = expect(R_A3, R_B3)
  E_A4 = (E_A1 + E_A2 + E_A3) / 3 # avg
  err[0] += abs(E_A1 - S_A)
  err[1] += abs(E_A2 - S_A)
  err[2] += abs(E_A3 - S_A)
  err[3] += abs(E_A4 - S_A)
  elo1[row.hometeam] = update(R_A1, S_A, E_A1)  
  elo1[row.awayteam] = update(R_B1, 1 - S_A, 1 - E_A1)
  elo2[row.hometeam] = update2(R_A2, row['diff'], E_A2)  
  elo2[row.awayteam] = update2(R_B2, -row['diff'], 1 - E_A2)
  elo3[row.hometeam] = update3(R_A3, row['diff'], E_A3)  
  elo3[row.awayteam] = update3(R_B3, -row['diff'], 1 - E_A3)

print(err)

for x in sorted([(elo1[k], k) for k in elo1], reverse=True):
  print(np.round(x[0], 1), x[1])

# print(expect(elo['Ireland'], elo['Italy']))