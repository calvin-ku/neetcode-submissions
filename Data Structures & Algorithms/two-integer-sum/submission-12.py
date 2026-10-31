class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in nums:
            for x in nums:
                if i+x==target:
                    if x>i:
                        answer.append(i)
                        answer.append(x)
                        return answer

                    else:
                        answer.append(x)
                        answer.append(i)
                        return answer

        return answer


        