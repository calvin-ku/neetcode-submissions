class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        andtheresultis = set()
        for i in nums:
            if i in andtheresultis:
                return True

            andtheresultis.add(i)

        return False
            