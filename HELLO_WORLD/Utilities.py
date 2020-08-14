def find_max(list):
    largest_no = list[0]
    for item in list:
        if item > largest_no:
            largest_no = item
    return largest_no

