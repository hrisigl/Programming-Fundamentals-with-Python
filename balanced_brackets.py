n = int(input())
is_balanced = False
balanced = 0

for i in range(n):
    curr_str = input()
    if curr_str == "(":
        balanced += 1

    elif curr_str == ")":
        if balanced == 1:
            is_balanced = True
            balanced = 0
        else:
            is_balanced = False
            break
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")