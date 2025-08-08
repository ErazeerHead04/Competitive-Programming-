class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        current = 0
        gain.insert(0,0)
        for i in range(len(gain)):
            
            current += gain[i]
            gain[i] = current
        
        return sorted(gain).pop()

#time: O(nlogn), everything else O(n) but sorting O(nlogn)
#space: O(n), extra space for sorting