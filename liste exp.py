#fonction qui recoit comme paramétres un liste
def afficher(X=[]):
    for x in X:
        print(x,end="/")
B=['yassine',False,34,'akram','zidane',3,12,'messi']
n=len(B)
#print("la lise contient :",n)
print(f"la lise contient {n} élements")
print("************$1ére methode*************")
for i in range(n):
   print(B[i])
#Autre facon
print("*************2éme methode***************")
for b in B:
   print(b,end="/")
   
   



    












