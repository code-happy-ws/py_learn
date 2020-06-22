S='gpwwyyrrr'
N=len(S)
A=[]
count = [(S.count(x), x) for x in set(S)]
for k,v in sorted(count):
    print('k v:',k,v)
    if float(k) > (N+1)/2:
        break
    print('k*v',k*v)
    A.extend(k*v)
B=[None]*N
B[::2]=A[N//2:]
B[1::2]=A[:N//2]
print(B)
