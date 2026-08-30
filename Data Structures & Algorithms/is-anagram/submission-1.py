class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # add characters of both to their own dicts
        # compare dict values & and associated numbers
        # if equal true, otherwise not

        inv_1 = Counter()
        for i in range(len(s)):
            inv_1[s[i]] += 1


        inv_2 = Counter()
        for i in range(len(t)):
            inv_2[t[i]] += 1

        
        if inv_1 == inv_2:
            return True

        return False