elements = input().split()
indexes = input().split()
moves = 0
is_it_ended = False

while indexes[0] != "end":
    moves += 1
    first_i = int(indexes[0])
    second_i = int(indexes[1])
    if first_i == second_i or 0 > first_i or first_i >= len(elements) or 0 >second_i or\
            second_i >= len(elements):
        insert_idx = len(elements) // 2
        elements.insert(insert_idx, "-" + str(moves) + "a")
        elements.insert(insert_idx, "-" + str(moves) + "a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if elements[first_i] == elements[second_i]:
            removed = elements[first_i]
            elements = [el for el in elements if not el in (removed)]
            print(f"Congrats! You have found matching elements - {removed}!")
        else:
            print("Try again!")
        if len(elements) == 0:
            is_it_ended = True
            break
    indexes = input().split()

if is_it_ended:
    print(f"You have won in {moves} turns!")
else:
    print(f"Sorry you lose :(")
    print(" ".join(elements))