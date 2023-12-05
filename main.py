import matplotlib.pyplot as plt
import numpy as np
import time

win_score = []
for i in range(51):
    win_score.append(0)

lose_score = []
for i in range(51):
    lose_score.append(0)

teams = ["Arizona Cardinals", "Baltimore Ravens", "Atlanta Falcons", "Buffalo Bills", "Carolina Panthers", "Cincinnati Bengals", "Chicago Bears"
         "Cleveland Browns", "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Houston Texans", "Green Bay Packers", "Indianapolis Colts", 
         "Los Angeles Rams", "Jacksonville Jaguars", "Minnesota Vikings", "Kansas City Chiefs", "New Orleans Saints", "Las Vegas Raiders", 
         "New York Giants", "Los Angeles Chargers", "Philadelphia Eagles", "Miami Dolphins", "San Francisco 49ers", "New England Patriots", 
         "Seattle Seahawks", "New York Jets", "Tampa Bay Buccaneers", "Pittsburgh Steelers", "Washington Commanders", "Tennessee Titans"]
cur_season = 1970

from pro_football_reference_web_scraper import team_game_log as t

for h in range(len(teams)):
    for i in range(52):
        try:
            game_log = t.get_team_game_log(team = teams[h], season = cur_season)
            time.sleep(1)
            for j in range(16):
                try:
                    score =  game_log['points_for'][j]
                    if game_log['result'][j] == "W":
                        win_score[score] += 1
                    else:
                        lose_score[score] += 1
                except:
                    print()
            cur_season += 1
        except:
            print("SHIT!")

ws_prune = []
for i in range(51):
    if win_score[i]:
        for j in range(win_score[i]):
            ws_prune.append(i)

ls_prune = []
for i in range(51):
    if lose_score[i]:
        for j in range(lose_score[i]):
            ls_prune.append(i)

print(len(win_score))
print(len(lose_score))

print("Win Mean & Stddev:")
print(np.mean(ws_prune))
print(np.std(ws_prune))

print()

print("Loss Mean & Stddev:") 
print(np.mean(ls_prune))
print(np.std(ls_prune))

plt.bar(np.arange(len(lose_score)) - 0.2, lose_score, 0.4)
plt.bar(np.arange(len(win_score)) + 0.2, win_score, 0.4)
plt.show()
