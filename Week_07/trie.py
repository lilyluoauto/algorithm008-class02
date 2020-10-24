#coding:utf-8
#!/usr/bin/python
#=================
# Project: project
# Creator: lily luo
# Create time: 2020/9/14
# Name: trie
# =======================
class Trie(object):
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self,word):
        node = self.root
        for char in word:
            node = node.setdefault(char,{})
        node[self.end_of_word] = word

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

trie = Trie()
trie.insert("apple")
flag = trie.search("apple")
print(flag)
f = trie.startsWith("app")
print(f)