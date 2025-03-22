N=int(input("taper un entier"))
max=N
min=N
for i in range(2,20) : 
 if N>max :
    max=N
 if N<min :
    min=N
print("le maximum est:",max)
print("le minimum est:",min)

