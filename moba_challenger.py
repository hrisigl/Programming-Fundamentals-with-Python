positions_pool = {}
total_points = {}

while True:
    data = input()
    if data == "Season end":
        break

    elif "->" in data:
        data = data.split(" -> ")
        player, position, skills = data
        skills = int(skills)

        if player not in positions_pool:
            positions_pool[player] = {position: skills}
        else:
            if position not in positions_pool[player]:
                positions_pool[player].update({position: skills})
            else:
                if positions_pool[player][position] < skills:
                    positions_pool[player][position] = skills

    elif "vs" in data:
        data = data.split(" vs ")
        player1, player2 = data
        if player1 in positions_pool and player2 in positions_pool:
            for position in positions_pool[player1]:
                if position in positions_pool[player2]:
                    player1_points = sum(d for d in positions_pool[player1].values() if d)
                    player2_points = sum(b for b in positions_pool[player2].values() if b)
                    if player1_points > player2_points:
                        del positions_pool[player2]
                    else:
                        del positions_pool[player1]
                    break

for player in positions_pool:
    curr_player_points = sum(d for d in positions_pool[player].values() if d)
    total_points.update({player: curr_player_points})
sorted_points = {k: v for k, v in sorted(total_points.items(), key=lambda item: -item[1])}


for player in sorted_points:
    print(f"{player}: {sorted_points[player]} skill")
    for p in positions_pool:
        if p == player:
            positions_pool[p] = {k: v for k, v in sorted(positions_pool[p].items(), key=lambda item: -item[1])}
            for c, p in positions_pool[p].items():
                print(f"- {c} <::> {p}")