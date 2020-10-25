# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-10-01 07:36
# IDE: PyCharm
# =========================================================

from math import *
from decimal import Decimal

class Similarity:

    def manhattan_distance(self,x, y):
        return sum(abs(a - b) for a, b in zip(x, y))

    def nth_root(self,value, n_root):
        root_value = 1 / float(n_root)
        return round(Decimal(value) ** Decimal(root_value), 3)

    def minkowski_distance(self,x, y, p_value):
        return self.nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)

    def square_rooted(self,x):
        return round(sqrt(sum([a * a for a in x])), 3)

    def cosine_similarity(self,x, y):
        numerator = sum(a * b for a, b in zip(x, y))

        denominator = self.square_rooted(x) * self.square_rooted(y)
        return round(numerator / float(denominator), 3)

    def jaccard_similarity(self,x, y):
        '''cardinality caculate how many elements are in set, for example |A|
        jaccard similarity cacualte the similarity between two finite samples '''
        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        return intersection_cardinality / float(union_cardinality)


if __name__ == '__main__':
    cacu_distance = Similarity()
    print(cacu_distance.minkowski_distance([0, 3, 4, 5], [7, 6, 3, -1], 3))
    print(cacu_distance.jaccard_similarity([0, 1, 2, 5, 6], [0, 2, 3, 5, 7, 9]))


