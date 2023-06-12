groceries = input().split("!")
is_command_go_shopping = False

while not is_command_go_shopping:
    command = input().split()
    if command[0] == "Go" and command[1] == "Shopping!":
        is_command_go_shopping = True
        break
    else:

        curr_command = command[0]
        if curr_command == "Urgent":
            if command[1] not in groceries:
                groceries.insert(0, command[1])

        elif curr_command == "Unnecessary":
            if command[1] in groceries:
                groceries.remove(command[1])

        elif curr_command == "Correct":
            if command[1] in groceries:
                a = groceries.index(command[1])
                groceries[a] = command[2]

        elif curr_command == "Rearrange":
            if command[1] in groceries:
                groceries.remove(command[1])
                groceries.append(command[1])
print(", ".join(groceries))