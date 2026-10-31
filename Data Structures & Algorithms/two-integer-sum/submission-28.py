class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i,z in enumerate(nums):
            for x,y in enumerate(nums[i+1:], start = i+1):
                if y+z==target:
                    if y>z:
                        answer.append(i)
                        answer.append(x)
                        return answer

                    else:
                        answer.append(x)
                        answer.append(i)
                        return answer

        return answer


        