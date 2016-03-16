# 从字符串中提取数字
# 首尾可以有空格
# 首部可以是正负号
# 遇到第一个不是数字就停止
# 不能溢出 32位
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        overflow = 1 << 31
        _max, _min = overflow - 1, -overflow
        sign, res = 1, 0
        if str[0] == '-' or str[0] == '+':
            sign = -1 if str[0] == '-' else 1
            str = str[1:]
        for i in str:
            if i.isdigit():
                res = res * 10 + int(i)
            else:
                break
            if res * sign > _max or res * sign < _min:
                return _max if sign > 0 else _min
        return res * sign


print Solution().myAtoi('2147483648')