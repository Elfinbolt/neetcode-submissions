class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        for num, count in freq.items():
            buckets[count].append(num)
        result = []

        for i in reversed(range(1, len(buckets))):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result