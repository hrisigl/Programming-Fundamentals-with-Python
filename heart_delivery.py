hearts_for_a_house = [int(i) for i in input().split("@")]
is_it_love = False
cupid_last_index = 0

while not is_it_love:
    command = input().split()
    if command[0] == "Love!":
        is_it_love = True
        break
    else:
        lenght = int(command[1])
        curr_position = cupid_last_index + lenght
        if curr_position >= len(hearts_for_a_house):
            curr_position = 0

        if hearts_for_a_house[curr_position] > 0:
            hearts_for_a_house[curr_position] -= 2
            if hearts_for_a_house[curr_position] == 0:
                print(f"Place {curr_position} has Valentine's day.")
        else:
            print(f"Place {curr_position} already had Valentine's day.")
        cupid_last_index = curr_position

print(f"Cupid's last position was {cupid_last_index}.")
if sum(hearts_for_a_house) == 0:
    print(f"Mission was successful.")
else:
    count = 0
    for house in hearts_for_a_house:
        if house > 0:
            count += 1
    print(f"Cupid has failed {count} places.")