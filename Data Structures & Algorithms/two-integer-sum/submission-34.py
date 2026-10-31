class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i,z in enumerate(nums):
            for x,y in enumerate(nums[i+1:], start=i+1):
                answer.append(i)
                answer.append(x+1)
                return answer

        return answer


        