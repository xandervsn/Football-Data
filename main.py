from pro_football_reference_web_scraper import team_game_log as t

game_log = t.get_team_game_log(team = 'Kansas City Chiefs', season = 1995)
print(game_log['points_for'][0])
