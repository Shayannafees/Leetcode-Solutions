class Solution:
    def isPalindrome(self, s: str) -> bool: # type: ignore
        a = ''.join(c for c in s if c.isalpha()).lower()
        
        i,j = 0, len(a) - 1
        while i < j:
            if a[i] == a[j]:
                i += 1
                j -= 1
            else:
                return False
        return True






s = Solution()
print(s.isPalindrome("Was it a car or a cat I saw?"))
print(s.isPalindrome("tab a cat"))