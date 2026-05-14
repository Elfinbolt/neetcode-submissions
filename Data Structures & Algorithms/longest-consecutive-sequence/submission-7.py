class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == [] :
            return 0
        nums1 = nums.copy()
        for i in range(1, len(nums1)):
            key = nums1[i]
            j = i - 1
            while j >= 0 and key < nums1[j]:
                nums1[j + 1] = nums1[j]
                j -= 1
            nums1[j + 1] = key
        longest = 1
        count = 1
        for k in range(1,len(nums1)):
            temp=nums1[k]
            l= k - 1
            if nums1[l] == nums1[k]:
                continue
            elif (nums1[k-1] + 1) == nums1[k]:
                count += 1
                longest = max(longest, count)  
            elif len(nums1) == 0:
                return 0
            else:
                count = 1
        return longest
        
