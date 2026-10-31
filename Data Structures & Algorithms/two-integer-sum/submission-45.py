class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        seen = {}
        #here i have a for loop check each of the values inside the list
        for i,value in enumerate(nums):
            
            complement = target - value
            #now I check to see if the complement is already been found
            if complement in seen:
                #since its been found i can retun the answer as a pair with the lowest index first followed by the higher index so i check which index is greater this is a redundant check since the complement is always found first which will innately be the smaller index so we can simply return the complement first followed by i
                answer.append(seen[complement])
                answer.append(i)
                print(answer)
                return answer
            seen[i] = value



            


        