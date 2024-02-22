# 1: Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # hashmap
        sumMap = {} # val : index

        # in enumerate, assign current index 'i' to corresponding value 'n' 
        for i, n in enumerate(nums):
            diff = target - n

            if diff in sumMap:
                return [sumMap[diff], i]
            
            # for this value 'n', the index will be 'i'
            sumMap[n] = i
