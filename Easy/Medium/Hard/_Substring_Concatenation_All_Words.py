# LC#30 - Substring with Concatenation of All Words
# Difficulty: Hard
# Topics: Hash Table, String, Sliding Window
#
# Approach: Sliding window with word-length chunks. Try each of
#           the 'word_len' possible starting offsets. Use hashmap
#           to track word frequency in current window, shrink
#           window from left when a word's count exceeds target
# Time: O(n) | Space: O(n)
#
# ML Connection: This sliding window + frequency counting pattern
# mirrors n-gram extraction and bag-of-words feature counting in
# NLP preprocessing pipelines before vectorization

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)
        
        if n < total_len:
            return []
        
        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1
        
        result = []
        
        for i in range(word_len):
            left = i
            count = 0
            window = {}
            j = i
            
            while j <= n - word_len:
                word = s[j:j + word_len]
                j += word_len
                
                if word in word_count:
                    window[word] = window.get(word, 0) + 1
                    count += 1
                    
                    while window[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    if count == num_words:
                        result.append(left)
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    window = {}
                    count = 0
                    left = j
        
        return result
