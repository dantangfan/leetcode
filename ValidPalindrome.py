# coding: utf-8
# 判断是否是回文
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        V = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s = filter(lambda x: x in V, s.lower())
        if not s:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        V = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in V:
                left += 1
                continue
            if s[right] not in V:
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True



print Solution().isPalindrome("A man, a plan, a canal: Panama")
print Solution().isPalindrome("race a car")
print Solution().isPalindrome("Zeus was deified\nsaw Suez.")

