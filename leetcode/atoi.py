# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = None
        value = 0
        for c in s:                
            if c == ' ' and sign == None:
                continue
            if c in ['+', '-'] and sign == None:
                sign = c
            elif c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                break
            else:
                if sign == None:
                    sign = '+'
                value = value * 10 + int(c)
        value *=  -1 if sign == '-' else 1
        if -2147483648 <= value < 2147483648:
            return value
        return -2147483648 if sign == '-' else 2147483647
                