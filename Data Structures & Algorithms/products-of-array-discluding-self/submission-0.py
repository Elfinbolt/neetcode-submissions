class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            temp = nums.copy()
            tempi = temp.pop(i)
            temp1 = []
            temp2=1
            for j in temp:
                temp2 *= j
            output.append(temp2)
        return output           