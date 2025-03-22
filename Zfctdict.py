def parity(n) :
    if n%2==0:
        return "pair"
    else:
        return "impair"
#declaration d'un dictionnaire vide
G =  {}
v= int(input("donner combien :"))
for i in range(v):
    x= int(input("donner un nomber :"))
    G[x]=parity(x)
print(G) 



