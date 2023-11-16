
from ast import Str
import math
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => '))
S=float(a**2) # ei olnud float
print("Ruudu pindala", S)
P=float(4*a)
print("Ruudu ümbermõõt", P)  #Oli "  '
di=float(a**2) # float
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #oli üks lisa )
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print('Ristküliku pindala', S) #ei olnud'
P=2*(b+c)
print("Ristküliku ümbermõõt", P)
di=float(math.sqrt(b*2+c*2))
print("Ristküliku diagonaal", round(di)) #ei olnud )
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => ')) # oli ' ' ja ))
d=float(2*r) # ei olnud *
print("Ringi läbimõõt",d) # ei olnud ,
S=math.pi*r*2
print("Ringi pindala", round(S))
C=2*math.pi*r #delete()
print("Ringjoone pikkus", round(C)) # ei olnud )