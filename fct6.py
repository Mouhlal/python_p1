S=0
enuméro=int(input("taper le numéro"))
enom=input("taper le nom")
eprénom=input("taper le prénom")
enotes=int(input("taper la note"))
for i in range(1,3):
    enotes=int(input("taper la note:"))
    S=S+enotes
    M=S/3
    print ("*******les infos sur l'éleve**********:")
    print("numéro:",enuméro)
    print("nom:",enom)
    print("prénom:",eprénom)
    print("Moyenne:",M)
    if M<=10 :
     print("Non admis")
    else:
     print("admis")
     







