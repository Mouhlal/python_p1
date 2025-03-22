
#création d'une liste vide
#la 1ére methode
#A=[] 
#la 2éme methode
#A=list() 
# une liste de noms
A=['akram',2,23,'said','akmaa','slo',True] 
n=len(A)#permet de retourner le nombre d'elements de la list
#print(f"la liste contient {n} élements")
#afficher le premier élements
#print(A[0])
#print(A[3])
#afficher le dérnier éléments
#print(A[-1])
#print(A[-4])
#autre facon
#print(A[n-1])
#parcourir tous les élements de la liste
#methode 1 par indice
print("methode 1")
for i in range(n):
    print(A[i])
#methode 2 par élement
print("methode 2")
for a in A:
    print(a,end='/')




