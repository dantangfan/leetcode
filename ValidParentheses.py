# coding:utf-8
# 正确的括号匹配，很简单，用栈模拟就行

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        pare = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        left = '({['
        res = []
        for p in s:
            if p in left:
                res.append(p)
            else:
                try:
                    q = res.pop()
                    if q != pare[p]:
                        return False
                except:
                    return False
        if res:
            return False
        return True

print Solution().isValid('()[()[]{}]()')