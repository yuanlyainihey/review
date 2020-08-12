class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        flag = False
        for i in range(1, len(s1)):
            flag = flag or (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]))
            flag = flag or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]))
        return flag