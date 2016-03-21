class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 == version2:
            return 0
        version1 = [int(_) for _ in version1.split('.')]
        version2 = [int(_) for _ in version2.split('.')]
        lv1, lv2 = len(version1), len(version2)
        for i in xrange(lv1-1, -1, -1):
            if not version1[i]:
                version1.pop(i)
            else:
                break
        for i in xrange(lv2-1, -1, -1):
            if not version2[i]:
                version2.pop(i)
            else:
                break
        while version1 and version2:
            if version1[0] > version2[0]:
                return 1
            elif version1[0] < version2[0]:
                return -1
            else:
                version1.pop(0)
                version2.pop(0)
        if version1:
            return 1
        elif version2:
            return -1
        else:
            return 0


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = [int(_) for _ in version1.split('.')]
        version2 = [int(_) for _ in version2.split('.')]
        lv1, lv2, v1, v2 = len(version1), len(version2), 0, 0
        c1, c2 = 1.0, 1.0
        for i in xrange(lv1):
            v1 += version1[i] / c1
            c1 *= 10.0
        for i in xrange(lv2):
            v2 += version2[i] / c2
            c2 *= 10.0
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            return 0


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2, c1, c2 = 0, 0, 1.0, 1.0
        for v in version1.split('.'):
            v = int(v)
            v1 += v / c1
            c1 *= 10.0
        for v in version2.split('.'):
            v = int(v)
            v2 += v / c2
            c2 *= 10.0
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            return 0

print Solution().compareVersion('0.1.1', '0.1.1.0')