from collections import ChainMap

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}

print('===========dictionary===========')
print(list(baseline.values()))
print(list(baseline))

print('===========ChainMap===========')
print(list(ChainMap(adjustments, baseline)))


print('===========ChainMap===========')



