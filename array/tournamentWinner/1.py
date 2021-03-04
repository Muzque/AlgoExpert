def tournamentWinner(competitions, results):
    winner_list = []
    for array, win in zip(competitions, results):
        winner = array[1 - win]
        winner_list.append(winner)
    return max(winner_list, key=winner_list.count)
