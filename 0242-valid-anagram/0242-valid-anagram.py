class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        idx = [0] * 26
        for i in range(len(s)):
            idx[ord(s[i]) - ord('a')] += 1
            idx[ord(t[i]) - ord('a')] -= 1

        for i in range(len(idx)):
            if idx[i] != 0:
                return False

        return True
        