"""
Problem: Word Ladder II (LC #126)
Difficulty: Hard
Link: https://leetcode.com/problems/word-ladder-ii/

Approach:
- BFS level by level from beginWord, trying every one-letter change
- Store parents[word] = words in the previous level that reach it
- Remove a level's words from the dictionary only after the level ends
- Stop at the level where endWord is found (shortest length)
- DFS from endWord back to beginWord through parents to build all paths
- Time: roughly O(N * L * 26 + number of paths) | Space: O(N * L)

ML Connection:
- Building a parent graph and backtracking all optimal paths is the
  same idea as extracting all best alignments in sequence models
  (e.g., Viterbi / beam search with backpointers).
"""

from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return []
        words.discard(beginWord)

        parents = defaultdict(set)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = defaultdict(set)
            for w in level:
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nw = w[:i] + c + w[i+1:]
                        if nw in words:
                            next_level[nw].add(w)
            for nw, ps in next_level.items():
                parents[nw] |= ps
            if endWord in next_level:
                found = True
            words -= set(next_level)
            level = set(next_level)

        if not found:
            return []

        res, path = [], [endWord]

        def dfs(word):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)
        return res
