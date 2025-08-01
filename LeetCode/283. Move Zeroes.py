class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_position = 0
        for i in nums:
            if i!=0:
                nums[insert_position] = i
                insert_position += 1
        for i in range(insert_position,len(nums)):
            nums[i] = 0
        #time: O(n)
        #space: O(1) for auxiliary space, rest is done in place