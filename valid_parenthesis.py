class Solution:
    def isValid(self, s: str) -> bool:
        
        
        hm = {
           ")": "(",
           "}": "{",
           "]": "["
        }

        stack = []

        for i in s:
            if i in hm:
            #pop from stack it's pair
                if len(stack) == 0:
                    return False
                starting = stack.pop() #(
                if starting == hm[i]:         #)
                    continue
                else:
                    return False
            else:
                stack.append(i)
            
        if len(stack) == 0:
            return True
        else:
            return False

s = Solution()
print(s.isValid('[(])'))