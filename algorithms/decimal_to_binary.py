def main(x):
    s = ''
    while x > 1:
        s = str(x % 2) + s
        x = x // 2
    if x == 1:
        s = str(x) + s
    return s


print(main(25))
