A=[]
def afficher():
    for i in A:
        print(i,end=" ")
n=int(input("taper le nombre d'élements"))
for i in range(n):
    X=int(input("taper un nombre"))
    A.append(X)
def somme():
    som= 0
    for i in A:
        som=som+i
    return som
print(f"la somme est {somme()}")
moy=somme()/n
print("le moyenne est:",moy)
















