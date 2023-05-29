treasure = input().split("|")
command = input().split()

while command[0] != "Yohoho!":
    curr_command = command[0]
    if curr_command == "Loot":
        items = command[1:]
        for item in items:
            if item not in treasure:
                treasure.insert(0, item)

    elif curr_command == "Drop":
        index = int(command[1])
        if index < len(treasure):
            removed_item = treasure.pop(index)
            treasure.append(removed_item)

    elif curr_command == "Steal":
        count = int(command[1])
        removed = []
        if count < len(treasure):
            for item in range(count, 0, -1):
                removed_item = treasure.pop(-item)
                removed.append(removed_item)
        else:
            removed = treasure.copy()
            treasure.clear()
        print(", ".join(removed))
    command = input().split()

if len(treasure) == 0:
    print("Failed treasure hunt.")
else:
    average = 0
    for item in treasure:
        average += len(item)
    average /= len(treasure)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
