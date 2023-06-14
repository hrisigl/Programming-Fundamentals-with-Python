pokemons = [int(i) for i in input().split()]
removed_pokemons_sum = 0

while len(pokemons) > 0:
    curr_idx = int(input())
    removed = 0
    if curr_idx < 0:
        removed = pokemons.pop(0)
        pokemons.insert(0, pokemons[-1])

    elif curr_idx >= len(pokemons):
        removed = pokemons.pop(-1)
        pokemons.append(pokemons[0])

    else:
        removed = pokemons[curr_idx]
        pokemons.pop(curr_idx)
    removed_pokemons_sum += removed
    for pokemon in range(len(pokemons)):
        if pokemons[pokemon] <= removed:
            pokemons[pokemon] += removed
        else:
            pokemons[pokemon] -= removed
print(removed_pokemons_sum)