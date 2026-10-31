class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        seen = {}
        #here i have a for loop check each of the values inside the list
        for i,value in enumerate(nums):
            complement = target - value
            if complement in seen.values():
                answer.append(seen[3])
                answer.append(i)
                return answer
            seen[i] = value



            


        