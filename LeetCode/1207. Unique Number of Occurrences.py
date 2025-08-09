from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = defaultdict(int)

        for i in arr:
            hashmap[i] += 1  
        occurence = list(hashmap.values())
        return len(occurence) == len(set(occurence))
            