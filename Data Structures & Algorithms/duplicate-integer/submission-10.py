class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if count(i)>1:
                return False

        return True