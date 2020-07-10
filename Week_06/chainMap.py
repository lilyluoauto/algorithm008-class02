from collections import ChainMap

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(ChainMap(adjustments, baseline))
print(list(ChainMap(adjustments, baseline)))
combined = baseline.copy()
combined.update(adjustments)
print(list(combined))
print(combined)

