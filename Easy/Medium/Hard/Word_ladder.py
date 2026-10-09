"""
Problem: Word Ladder (LC #127)
Difficulty: Hard
Link: https://leetcode.com/problems/word-ladder/

Approach:
- BFS from beginWord, each level = one transformation
- For each word, try replacing each char with a-z
- If new word in word_set and not visited → add to queue
- Return steps+1 when endWord reached
- Time: O(M^2 * N) | Space: O(M^2 * N)
  where M = word length, N = wordList size

ML Connection:
- Word transformation graph is similar to word embedding
  space where similar words are close neighbors
- BFS shortest path mirrors how knowledge graphs
  find shortest semantic paths in NLP systems
"""

from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word == endWord:
                        return steps + 1
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, steps + 1))

        return 0
