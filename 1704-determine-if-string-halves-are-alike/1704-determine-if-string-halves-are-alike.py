class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)//2
        A, B = s[:l].lower(), s[l:].lower()
        a = b = 0
        for i in range(l):
            if A[i] in 'aeiou': a+=1
            if B[i] in 'aeiou': b+=1
        return a==b