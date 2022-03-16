from collections import Counter

ini_list = [1, 2, 3, 4, 4, 5, 5, 5, 5, 7,
            1, 1, 2, 4, 7, 8, 9, 6, 6, 6]

# printing initial ini_list
print("initial list", str(ini_list))

# sorting on bais of frequency of elements
result = [item for items, c in Counter(ini_list).most_common() for item in [items] * c]
print('Counter(ini_list).most_common()')
res = [item for c in Counter(ini_list).most_common()]
print(Counter(ini_list).most_common())
# s = Counter(ini_list)
# print(s)
# a = 'abc'
# print([c in s.most_common()])
# printing final result
# print("final list", str(result))
