from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]):
        stack = []

        for i,ch in enumerate(tokens):
            if ch in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if ch == "+":
                    stack.append(a + b)
                elif ch == "-":
                    stack.append(a - b)
                elif ch == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))

            else:
                stack.append(int(ch))
        
        return stack[-1]

s = Solution()
s.evalRPN(["1","2","+","3","*","4","-"])