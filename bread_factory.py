energy = 100
coins = 100
day_events = input().split("|")
is_day_completed = True

for event in day_events:
    curr_event = event.split("-")
    command = curr_event[0]
    number = int(curr_event[1])

    if command == "rest":
        gained_energy = 0
        if energy + number <= 100:
            gained_energy = number
            energy += gained_energy
        else:
            gained_energy = 100 - energy
            energy += gained_energy

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif command == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            is_day_completed = False
            break

if is_day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")