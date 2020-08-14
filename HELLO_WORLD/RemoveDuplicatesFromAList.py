list_a = [1, 2, 2, 4, 2, 3, 5, 3]
uniques = []
for item in list_a:
    if item not in uniques:
        uniques.append(item)
print(uniques)