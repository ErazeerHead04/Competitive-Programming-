class Solution:
    def numTrees(self, n: int) -> int:
        
        if n==0:
            return 0
        memo = {}
        def countBST(start, end):
            trees = []
            
            if (start, end ) in memo:
                return memo[(start,end)]
            if start>end:
                return 1
            total = 0
            for i in range(start,end+1):
                left_subtree = countBST(start,i-1)
                right_subtree = countBST(i+1, end)

                total += left_subtree*right_subtree

                
                
            memo[(start,end)] = total
            return total


        return countBST(1,n)
        

        