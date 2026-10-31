class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i,z in enumerate(nums):
            for x,y in enumerate(nums[i+1:]):
                if z+y == target:
                    answer.append(i)
                    answer.append(x)
                    return answer

        return answer


        