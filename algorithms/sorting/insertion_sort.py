def main(l):
    for i in range(1, len(l)):
        temp = l[i]
        k = i
        while temp < l[k - 1] and k > 0:
            l[k] = l[k - 1]
            k -= 1
        l[k] = temp
    return l


l = [19, 2, 31, 45, 6, 11, 121, 27]
r = main(l)
print(r)
