# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        missing, extra = self.hash_sequence(p), {}
        anagrams = [] 
        
        for i in range(len(s)):
            self.append_char(s[i], missing, extra)
            if i >= len(p):
                self.deselect_char(s[i - len(p)], missing, extra)
            if i >= len(p) - 1 and len(extra) == 0 and len(missing) == len(extra):
                anagrams.append(i - len(p) + 1)
        return anagrams
            
    def append_char(self, c, missing, extra):
        if c not in missing.keys():
            extra[c] = extra.get(c, 0) + 1
        else:
            if missing[c] == 1:
                del missing[c]
            else:
                missing[c] -= 1
            
    def deselect_char(self, c, missing, extra):
        if c in extra:
            if extra[c] == 1:
                del extra[c]
            else:
                extra[c] -= 1
        else:
            missing[c] = missing.get(c, 0) + 1
        
    def hash_sequence(self, s: str):
        seq = {}
        for c in s:
            seq[c] = seq.get(c, 0) + 1
        return seq
