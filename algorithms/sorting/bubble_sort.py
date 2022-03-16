def main(l):
    for i in range(len(l) - 1, 1, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


l = [19, 2, 31, 45, 6, 11, 121, 27]
r = main(l)
print(r)
