people_waiting = int(input())
lift_state = [int(i) for i in input().split()]


for course in range(len(lift_state)):
    if lift_state[course] < 4:
        needed_people = 4 - lift_state[course]
        if people_waiting >= needed_people:
            people_waiting -= needed_people
            lift_state[course] += needed_people
        elif 0 < people_waiting < 4:
            lift_state[course] += people_waiting
            people_waiting = 0
        if people_waiting == 0:
            break

has_lift_empty_spots = False
for cell in lift_state:
    if cell < 4:
        has_lift_empty_spots = True
lift_state = [str(i) for i in lift_state]

if has_lift_empty_spots:
    print("The lift has empty spots!")
    print(" ".join(lift_state))
elif people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join(lift_state))
elif people_waiting == 0 and not has_lift_empty_spots:
    print(" ".join(lift_state))