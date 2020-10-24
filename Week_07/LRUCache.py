#coding:utf-8
#!/usr/bin/python
#=================
# Project: project
# Creator: user01
# Create time: 2020/10/9
# Name: LRUCache
# =======================
import collections


class LRUCache(object):

	def __init__(self, capacity):
		self.dic = collections.OrderedDict()
		self.remain = capacity

	def get(self, key):
		if key not in self.dic:
			return -1
		v = self.dic.pop(key)
		self.dic[key] = v   # key as the newest one
		return v

	def put(self, key, value):
		if key in self.dic:
			self.dic.pop(key)
		else:
			if self.remain > 0:
				self.remain -= 1
			else:   # self.dic is full
				self.dic.popitem(last=False)
		self.dic[key] = value

if __name__ == '__main__':
	cache = LRUCache(2)

	cache.put(1, 1)
	cache.put(2, 2)
	print(cache.get(1))
	cache.put(3, 3)
	cache.get(2)
	cache.put(4, 4)
	cache.get(1)
	cache.get(3)
	cache.get(4)