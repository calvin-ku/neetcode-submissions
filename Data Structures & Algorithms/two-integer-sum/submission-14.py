class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in enumerate(nums):
            for x in enumerate(nums):
                if nums[i]+nums[x]==target:
                    if nums[x]>nums[i]:
                        answer.append(i)
                        answer.append(x)
                        return answer

                    else:
                        answer.append(x)
                        answer.append(i)
                        return answer

        return answer


        