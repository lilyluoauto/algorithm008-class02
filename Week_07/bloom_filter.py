# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-10-02 09:06
# IDE: PyCharm
# =========================================================

# Python
from bitarray import bitarray
import mmh3
class BloomFilter:
	def __init__(self, size, hash_num):
		self.size = size
		self.hash_num = hash_num
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)
	def add(self, s):
		for seed in range(self.hash_num):
			result = mmh3.hash(s, seed) % self.size
			self.bit_array[result] = 1
	def lookup(self, s):
		for seed in range(self.hash_num):
			result = mmh3.hash(s, seed) % self.size
			if self.bit_array[result] == 0:
				return "Nope"
		return "Probably"
bf = BloomFilter(500000, 7)
bf.add("dantezhao")
print (bf.lookup("dantezhao"))
print (bf.lookup("yyj"))


import pybloof

filter = pybloof.UIntBloomFilter(size=100, hashes=9)