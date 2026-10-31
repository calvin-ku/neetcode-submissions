class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i,z in enumerate(nums):
            for x,y in enumerate(nums):
                if nums[y]+nums[z]==target:
                    if nums[y]>nums[z]:
                        answer.append(i)
                        answer.append(x)
                        return answer

                    else:
                        answer.append(x)
                        answer.append(i)
                        return answer

        return answer


        