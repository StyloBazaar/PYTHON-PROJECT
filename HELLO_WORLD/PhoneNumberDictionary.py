digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
numbers_in_words = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'NIne',
}
phone_num = input("Enter phone NUmber: ")
phone_num_in_words = ''
for num in phone_num:
    phone_num_in_words += f'{numbers_in_words[int(num)]} '
print(phone_num_in_words)
