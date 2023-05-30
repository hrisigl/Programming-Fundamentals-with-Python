pirate_ship = [int(i) for i in input().split(">")]
warship = [int(j) for j in input().split(">")]
max_health_for_section = int(input())
is_command_retire = False
is_ship_sinking = False

while not is_command_retire and not is_ship_sinking:
    command = input().split()
    curr_command = command[0]
    if curr_command == "Retire":
        is_command_retire = True
        break
    else:
        if curr_command == "Fire":
            index = int(command[1])
            damage = int(command[2])
            if 0 <= index < len(warship):
                warship[index] -= damage
                if warship[index] <= 0:
                    print("You won! The enemy ship has sunken.")
                    is_ship_sinking = True
                    break

        elif curr_command == "Defend":
            start_i = int(command[1])
            end_i = int(command[2])
            damage = int(command[3])
            if 0 <= start_i < len(pirate_ship) and 0 <= end_i < len(pirate_ship):
                for i in range(start_i, end_i + 1):
                    pirate_ship[i] -= damage
                    if pirate_ship[i] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        is_ship_sinking = True
                        break

        elif curr_command == "Repair":
            index = int(command[1])
            health = int(command[2])
            if 0 <= index < len(pirate_ship):
                if pirate_ship[index] + health <= max_health_for_section:
                    pirate_ship[index] += health
                else:
                    pirate_ship[index] = max_health_for_section

        elif curr_command == "Status":
            need_repair_counter = 0
            twenty_percents = max_health_for_section * 0.2
            for section in pirate_ship:
                if section < twenty_percents:
                    need_repair_counter += 1
            print(f"{need_repair_counter} sections need repair.")

if is_command_retire:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
