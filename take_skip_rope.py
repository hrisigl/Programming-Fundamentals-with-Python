string_input = input()
nums_list = [int(i) for i in string_input if i.isnumeric()]
non_nums_list = [str(a) for a in string_input if not a.isnumeric()]
result = []

for take_skip in range(len(nums_list)):
    if take_skip % 2 == 0:
        take = nums_list[take_skip]
        for char in range(take):
            result.append(non_nums_list.pop(0))
            if len(non_nums_list) == 0:
                break

    else:
        skip = nums_list[take_skip]
        if skip > 0:
            for char in range(skip):
                non_nums_list.pop(0)
    if len(non_nums_list) == 0:
        break
print("".join(result))
