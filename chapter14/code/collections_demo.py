import collections,itertools

from collections import OrderedDict, Counter

# od = OrderedDict()
#
# od["k1"] = "v1"
# od["k2"] = "v2"
# print(od)

str1 = "abcghkkdsjdjjds"
"""
{"a":2, "b":1}
"""
res = Counter(str1).most_common(3)
print(res)


