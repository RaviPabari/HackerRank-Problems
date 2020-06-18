class Solution:
    def backMeUp(self,s):
        stack = []
        for i in s:
            if i!='#':
                stack.append(i)
            if i=='#':
                if stack:
                    stack.pop()
        return ''.join(stack)
    def backspaceCompare(self, S: str, T: str) -> bool:
        if self.backMeUp(S)==self.backMeUp(T):
            return True
        else:
            return False
