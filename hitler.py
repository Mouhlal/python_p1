D={}
number = int(input("combien de students:"))
for i in range (number) :
    nom=input("taper le nom")
    note=float(input("taper une note"))
    D[nom]=note
#affivhage du dictionaire
print("nom\t\tnote")
for c,v in D.items():
    print(f"{c}\t\t{v}")

som=0
for c,v in D.items():
    som +=v
moy=som/len(D) #ou moy=som/number
print(f"la moyenne de la classe est :{moy:.2f}")

A=list(D.values())  #mettre les valeurs au dictionnaire D
#dans la liste A
max=A[0]    #max le premier élément de la liste
nom=list(D.keys())
for c,v in D.items():
    if  v>max :
        max=v
        nom=c
print(f"le meilleur stagiares est:{nom}\t\t{D[nom]}")











