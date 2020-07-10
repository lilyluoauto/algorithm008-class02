from collections import ChainMap

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
chainmap = ChainMap(adjustments, baseline)
print(chainmap)
print(list(chainmap))
print(chainmap["art"])

combined = baseline.copy()
combined.update(adjustments)
print("cobimed is :",combined)
print(list(combined))

child1 = chainmap.new_child({"test":"test-1"})
print(child1)
child2 = child1.new_child({"test-2":"test-2"})
print(child2)


