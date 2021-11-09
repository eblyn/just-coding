# https://leetcode.com/problems/remove-invalid-parentheses/

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:    
        open_seg, clos_seg = self.unmatched_idx(s)
        
        left = self.del_extra_closed(s, clos_seg) if len(clos_seg) != 0 else ['']
        right = self.del_extra_opened(s, open_seg) if len(open_seg) != 0 else ['']
        
        middle = self.middle_subseq(s, clos_seg, open_seg)
        return self.combine([l + middle for l in left], right)

        
    def middle_subseq(self, s:str, clos_seg: List[int], open_seg: List[int]) -> List[str]:
        start = clos_seg[-1] + 1 if len(clos_seg) > 0 else 0
        end = open_seg[0] if len(open_seg) > 0 else len(s)
        return s[start:end]
    
    
    def unmatched_idx(self, s: str) -> (List[int], List[int]):
        extra_opened = []
        extra_closed = []
        
        for idx in range(len(s)):
            if s[idx] == '(':
                extra_opened.append(idx)
            if s[idx] == ')':
                if len(extra_opened) == 0:
                    extra_closed.append(idx)
                else:
                    extra_opened.pop()
        
        return extra_opened, extra_closed
    

    def del_extra_closed(self, s: str, ext: List[int]) -> List[str]:
        if len(ext) == 1:
            return self.delete_one([s[:ext[0]+1]], ')')
            
        pre = self.del_extra_closed(s, ext[:-1])
        combined = self.combine(pre, [s[ext[-2]+1 : ext[-1]+1]])
        return self.delete_one(combined, ')')
    
    
    def del_extra_opened(self, s: str, ext: List[int]) -> List[str]:
        if len(ext) == 1:
            return self.delete_one([s[ext[-1]:]], '(')
            
        pre = self.del_extra_opened(s, ext[1:])
        combined = self.combine([s[ext[0]:ext[1]]], pre)
        return self.delete_one(combined, '(')
    

    def delete_one(self, seqs: List[str], c: str) -> List[str]:
        result = []
        for seq in seqs:
            self.delete_one_from_str(seq, c, result)
        return result
    
    
    def delete_one_from_str(self, seq: str, c: str, result: List[str]) -> List[str]:
        idx = 0
        while idx < len(seq):
            if seq[idx] == c:
                s = seq[:idx] + seq[idx+1:]
                s if len(s) > 0 else ''
                if s not in result:
                    result.append(s)
                while idx < len(seq) and seq[idx] == c:
                    idx += 1
            else:
                idx += 1
    
    
    def combine(self, set1: List[str], set2: List[str]) -> List[str]:
        if len(set1) == 0:
            return set2
        if len(set2) == 0:
            return set1
        
        result = []
        for seq1 in set1:
            result += [seq1 + seq2 for seq2 in set2]  
        return result
        