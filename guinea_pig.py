food_per_month_grams = float(input()) * 1000
hay_per_month_grams = float(input()) * 1000
cover_per_month_grams = float(input()) * 1000
pigs_weigt_grams = float(input()) * 1000
is_everything_enough = True


for day in range(1,31):
    food_per_month_grams -= 300
    if food_per_month_grams < 0:
        is_everything_enough = False
        break

    if day % 2 == 0:
        hay_per_month_grams -= (food_per_month_grams * 0.05)
        if hay_per_month_grams < 0:
            is_everything_enough = False
            break

    if day % 3 == 0:
        cover_per_month_grams -= (pigs_weigt_grams / 3)
        if cover_per_month_grams < 0:
            is_everything_enough = False
            break
if is_everything_enough:
    print(f"Everything is fine! Puppy is happy! Food: {food_per_month_grams / 1000:.2f}"
          f", Hay: {hay_per_month_grams / 1000:.2f}"
          f", Cover: {cover_per_month_grams / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")