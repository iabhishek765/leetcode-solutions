# LC#1807 - Evaluate the Bracket Pairs of a String
# Difficulty: Medium
# Topics: String, Hash Table
#
# Approach: Build dict from knowledge list. Scan string:
#           on '(' find matching ')' via index(), extract key,
#           replace with dict value or '?'. Append non-bracket
#           chars directly. Join result list.
# Time: O(n) | Space: O(k)
#
# ML Connection: Template string evaluation mirrors prompt
# templating in LLM pipelines where placeholders like
# {context} or {query} are replaced with actual values
# before sending to the model.

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kmap = {k: v for k, v in knowledge}
        result = []
        i = 0
        
        while i < len(s):
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i+1:j]
                result.append(kmap.get(key, '?'))
                i = j + 1
            else:
                result.append(s[i])
                i += 1
        
        return ''.join(result)
