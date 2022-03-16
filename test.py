def remove_duplicate(s):
    res = ''
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            res += s[i - 1]

    res += s[-1]
    return res


print(remove_duplicate('aaaabbbccddssaaavvvaaaaaa'))
