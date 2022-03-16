def main(l):
    for i in range(len(l)-1, 0, -1):
        max_val_index = 0
        for j in range(1, i+1):
            if l[j] > l[max_val_index]:
                max_val_index = j
        l[i], l[max_val_index] = l[max_val_index], l[i]
    return l


l = [19, 2, 31, 45, 6, 11, 121, 27]
r = main(l)
print(r)
