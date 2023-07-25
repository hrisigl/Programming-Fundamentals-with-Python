n = int(input())

plants = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    rarity = int(rarity)

    if plant not in plants:
        plants[plant] = {"rarity": 0, "ratings": []}
    plants[plant]["rarity"] = rarity

while True:
    command_text = input().split(": ")
    command = command_text[0]

    if command == "Exhibition":
        break

    if command == "Rate":
        plant, rating = command_text[1].split(" - ")
        rating = int(rating)
        if plant not in plants:
            print("error")
            continue

        plants[plant]["ratings"].append(rating)

    elif command == "Update":
        plant, new_rarity = command_text[1].split(" - ")
        new_rarity = int(new_rarity)

        if plant not in plants:
            print("error")
            continue
        plants[plant]["rarity"] = new_rarity

    elif command == "Reset":
        plant = command_text[1]
        if plant not in plants:
            print("error")
            continue
        plants[plant]["ratings"].clear()

print("Plants for the exhibition:")
for plant in plants:
    rarity = int(plants[plant]["rarity"])
    ratings = plants[plant]["ratings"]
    if ratings:
        avg_rating = float(sum(ratings) / len(ratings))
    else:
        avg_rating = 0

    print(f"- {plant}; Rarity: {rarity}; Rating: {avg_rating:.2f}")