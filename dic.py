etudiants={"etudiant1":12,"etudiant2":10,"etudiant3":6,"etudiant4":8,"etudiant5":15}
#declaration de deux dictionnaire vides
etudiantsAdmis={}
etudiantnonAdmis={}
for c,v in etudiants.items():
    if v>=10:
        etudiants[c]=v
    else:
        etudiantnonAdmis[c]=v


print("les etudiants non admis:")
for c,v in etudiantnonAdmis.items():
    print(f"{c}------>{v}")
    