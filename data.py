
import requests
import re
import datetime

f1 = open('teams.txt', 'r')
f2 = open('match_data_20251102.csv', 'w')

f2.write('date,hometeam,awayteam,home,away\n')

teams = [line.strip() for line in f1]

def extract(text, rules=[r'[0-9]+ - [0-9]+', r'[0-9]{2} \w{3} [0-9]{2}', r'maxw=43&v=[0-9]+" alt="[A-Za-z ]+']):
  output = []
  num = 0
  for line in text.split('<div'):
    for ruleid, rule in enumerate(rules):
      found = re.findall(rule, line)
      if found:
        output.append((found[0], ruleid, num))
        num += 1
  return output


for teama in teams:
  for teamb in teams:
    if teama < teamb:
      print(teama, teamb)
      url = 'https://www.rugbypass.com/live/' + teama + '-vs-' + teamb + '/head-to-head/'

      text = requests.get(url)

      # scores = re.findall(r'[0-9]+ - [0-9]+', text.text)
      # dates = re.findall(r'[0-9]{2} \w{3} [0-9]{2}', text.text)
      # countries = re.findall(r'maxw=43&v=[0-9]+" alt="[A-Za-z ]+', text.text)

      extracted = extract(text.text)
      # print(extracted)

      # for i in range(len(countries) // 2):
      for i, item in enumerate(extracted):
        text, ruleid, _ = item
        if ruleid == 0:
          score = re.findall(r'[0-9]+', text)
          pointsa, pointsb = score[0], score[1]
        elif ruleid == 1:
          date = text
        else:
          team = text[27:]
        # if rule chain is 0, 1, 2
        if ruleid == 2 and extracted[i - 1][1] == 1 and extracted[i - 2][1] == 0:
          away = team
          home = extracted[i - 3][0][27:]
          f2.write(date + ',' + home + ',' + away + ',' + pointsa + ',' + pointsb + '\n')

f2.close()
