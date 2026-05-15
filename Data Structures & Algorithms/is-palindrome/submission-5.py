import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s3=""
        s1 = s.lower().replace(" ","").translate(str.maketrans('', '', string.punctuation))
        for i in range(len(s1)):
            if s1[i].isalnum(): 
                s3=s1
                continue
            else:
                s3=s1[:i] + s1[i+1:]
        s2 = s3
        s2 = s2[::-1]
        print(s3)
        print(s2)
        if s3 == s2:
            return True
        else:
            return False