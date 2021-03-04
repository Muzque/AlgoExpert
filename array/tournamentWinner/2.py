def tournamentWinner(competitions, results):
    bestTeam = None
    table = {bestTeam: 0}
    for teams, idx in zip(competitions, results):
        winner = teams[1 - idx]
        table[winner] = table.get(winner, 0) + 3
        if table[winner] > table[bestTeam]:
            bestTeam = winner
    return bestTeam
