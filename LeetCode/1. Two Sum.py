
#Using Hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            hashmap[n] = i
        
        for i,n in enumerate(nums):
            remaining = target - n
            if remaining in hashmap and i!= hashmap[remaining]:
                return [i, hashmap[remaining]]
        return []
#time: O(n)
#Space: O(n)

#Using brute force:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

#time: O(n^2)
#space: O(1)