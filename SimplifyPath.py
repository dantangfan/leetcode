# coding:utf-8
# 要动态的删除列表内容,可以用 filter 函数,但是这样就另外申请了内存, 还可以从后往前遍历,就不会出错了
# 这里是返回 unix 绝对路径的问题
# 先淘汰多余的 / ,然后去掉多余的 . ,然后用一个栈来记录当前的操作,是该添加还是该回退
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        for i in xrange(len(path)-1, -1, -1):
            if not path[i]:
                del path[i]
        stack = []
        for i, v in enumerate(path):
            if v == '.':
                continue
            elif v == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(v)
        res = '/'.join(stack)
        return '/' + res

print Solution().simplifyPath("/home/")
print Solution().simplifyPath("/a/./b/../../c/")
print Solution().simplifyPath("////")
