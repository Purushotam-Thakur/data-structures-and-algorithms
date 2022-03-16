def merge_sort(a):
    l = len(a)
    if l > 1:
        mid = l // 2
        left_half = a[:mid]
        right_half = a[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a[k] = left_half[i]
                i += 1
            else:
                a[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            a[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            a[k] = right_half[j]
            j += 1
            k += 1
        return a


l = [19, 2, 31, 45, 6, 11, 121, 27]
r = merge_sort(l)
print(r)
