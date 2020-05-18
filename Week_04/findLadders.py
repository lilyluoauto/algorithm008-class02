# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-05-12 23:00
# IDE: PyCharm
# =========================================================
from collections import defaultdict


def defaultlist(list):
    pass


class Solution():
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return []

        output = defaultdict(list)

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = [(beginWord, 0)]
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        # output.append([])
                        if output is None:
                            output[level] = list(visited.keys())
                        else:
                            for idx,item in output:
                                if len(list(visited.keys()))<len(item):
                                    del output[idx]
                                    output[level]=list(visited.keys())
                                elif len(list(visited.keys())) == len(item):
                                    output[level] = list(visited.keys())
                                else:
                                    pass

                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return list(output.values())


so = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
out = so.findLadders(beginWord, endWord, wordList)
print(out)