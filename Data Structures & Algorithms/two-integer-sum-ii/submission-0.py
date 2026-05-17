class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash1={}
        for i in range(len(numbers)):
            temp1 = numbers[i]
            for j in range(len(numbers)):
                if i != j:
                    sum1=temp1 + numbers[j]
                    if sum1 == target:
                        solution = []
                        solution.append(i+1)
                        solution.append(j+1)
                        return solution
                    else :
                        continue
                else:
                    continue