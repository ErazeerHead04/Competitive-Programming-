class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        out = ""
        n1 = len(word1)
        n2 = len(word2)

        for i in range(max(n1,n2)):
            if i<n1:
                out += word1[i]
            if i<n2:
                out += word2[i]
        return out     #time complexity: O((n1+n2)^2)
                        #took 15 ms in leetcode

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        out = []
        n1 = len(word1)
        n2 = len(word2)

        for i in range(max(n1,n2)):
            if i<n1:
                out.append(word1[i])
            if i<n2:
                out.append(word2[i])
        return "".join(out)     #time complexity: O(n1+n2)
                                #append is amortized O(1), and the single "".join(...) pass is O(N), giving you overall O(n1 + n2) time.
                                #took 17 ms in leetcode