number_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, number_list))))
