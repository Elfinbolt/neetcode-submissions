class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1={}
        for i in range(len(strs)):
            sort1="".join(sorted(strs[i]))
            if sort1 == "".join(sorted(strs[i])):
                if sort1 not in hash1:
                    hash1[sort1]=[]
                hash1[sort1].append(strs[i])
            
        answer = list(hash1.values())
        return answer