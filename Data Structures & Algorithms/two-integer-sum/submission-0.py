class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1={}
        for i in range(len(nums)):
            temp1 = nums[i]
            for j in range(len(nums)):
                if i != j:
                    sum1=temp1 + nums[j]
                    if sum1 == target:
                        solution = []
                        solution.append(i)
                        solution.append(j)
                        return solution
                    else :
                        continue
                else:
                    continue
                