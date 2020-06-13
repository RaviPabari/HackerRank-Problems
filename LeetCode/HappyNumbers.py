def fun(num):
    s = 0
    while(num!=0):
        s += (num%10)**2
        num = num//10
    return s
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while(True):
            n = fun(n)
            if n in visited:
                return False
            visited.add(n)
            if n==1:
                return True
