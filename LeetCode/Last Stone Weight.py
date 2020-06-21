class Solution:
    def lastStoneWeight(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        arr.sort()
        while(len(arr)!=1):
            arr.sort()
            #print(arr)
            if len(arr)>1:
                s1 = arr.pop()
                s2 = arr.pop()
                if s1!=s2:
                    x = abs(s1-s2)
                    arr.append(x)
            if not arr:
                return 0
        return arr[0]
        
