# 217: Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        duplicates = False

        hashset = set()

        for i in nums:
            if i in hashset:
                duplicates = True
                break
            hashset.add(i)
        
        return duplicates
        