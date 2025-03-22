A = {}
H = input("Taper something :").lower()
V = ["a","e","i","o","u","y"]
for i in V:
    C = 0
    for j in H:
       if j==i:C=+1
    A[V]=C
for c,v in A.items():
    print(c,v)