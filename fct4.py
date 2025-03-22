def ok(N):
    ok=True
    for i in range(2,N-1):
        if N%i==0 :
             ok=False
    return ok

N=int(input("taper un nombre "))
print(ok(N))#appel d'un fonction
















