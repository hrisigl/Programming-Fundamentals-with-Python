targets = [int(a) for a in input().split()]

while True:
    command = input().split()
    if command[0] == "End":
        break
    else:
        curr_com = command[0]
        index = int(command[1])
        if curr_com == "Shoot":
            power = int(command[2])
            if 0 <= index < len(targets):
                targets[index] -= power
                if targets[index] <= 0:
                    targets.pop(index)

        elif curr_com == "Add":
            value = int(command[2])
            if 0 <= index < len(targets):
                targets.insert(index, value)
            else:
                print("Invalid placement!")

        elif curr_com == "Strike":
            radius = int(command[2])

            start_i = index - radius
            end_i = index + radius
            if start_i in range(len(targets)) and end_i in range(len(targets)):
                r = radius * 2 + 1
                for i in range(r):
                    targets.pop(start_i)
            else:
                print("Strike missed!")

targets = [str(a) for a in targets]
print("|".join(targets))