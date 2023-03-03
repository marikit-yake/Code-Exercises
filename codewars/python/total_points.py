def points(games):
    season_points = 0

    for game in games:
        score1, score2 = map(int, game.split(":"))

        if score1 > score2:
            season_points += 3

        elif score1 == score2:
            season_points += 1

    return season_points