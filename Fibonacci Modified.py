def fib(t1,t2,n):
    i=2
    while(i<n):
        t1,t2 = t2,t1 + t2**2
        i+=1
    return t2

t1,t2,n = map(int,input().split())
print(fib(t1,t2,n))
