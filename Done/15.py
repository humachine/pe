N=20
mem={}
def func(x,y, n):
    if (x,y) in mem:
        return mem[(x,y)]
    if x==n and y==n:
        mem[(x,y)]=0
        return 0
    if y==n-1:
        mem[(x,y)]=1
        return 1
    if x==n-1:
        mem[(x,y)]=1
        return 1
    mem[(x,y)]=func(x+1,y,n) + func(x,y+1,n)
    return mem[(x,y)]

print func(0,0,N+1)
#for N in range(2,10):
 #   print func(0,0,N+1)

    
