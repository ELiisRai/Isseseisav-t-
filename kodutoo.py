print("Tere!")

#Ulesanne 2.1
print("\nRuudu sees asub ring. Ringi raadius on R.")
print("Siis a = 2R")
print("Ruudu pindala = 2R * 2R")
print("Ruudu umbermoot = 4R")
print("Ringi pindala = (R2)**")
print("Ringi umbermoot = 8R")

#Ulesanne 2.2
print("\nMaa raadius ekvaatori kohal on 6378 km. Siis...")
mu=6378*8
print("See tahendab, et maa umbermoot on ", mu)
print("2 euro = d = 25,75 mm")
d=mu/0.00002575
print(round(d,0), "- munte on vaja, et rida ulatuks umber maa ")

# Ulesanne 3
print("\nkill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll ")
print("killkoll")
print("kill-koll")   # Selllel ulesannel ma ei kasutanud muutujad. Motlen,muutujate kasutamine on kindlasti ostarbekas kui on vaja midagi muutuda.

#Ulesanne 4
l1="Rong see sõitis tsuhh tsuhh tsuhh,\npiilupart oli rongijuht.\nRattad tegid rat tat taa,\nrat tat taa ja tat tat taa.\nAga seal rongi peal,\nkas sa tead, kes olid seal?"
l2="Rong see sõitis tuut tuut tuut,\npiilupart oli rongijuht.\nRattad tegid kill koll koll,\nkill koll koll ja kill koll kill."
v=str(input("\nMilline laul sa soovid? 1 voi 2?\n"))
if v=="1":
    print(l1)
elif v=="2":
    print(l2)
else:
    print("Vali 1 voi 2!")

#Ulesanne 5
a=float(input("\na= "))
b=float(input("b= "))
u=a+a+b+b
p=a*b
print("P= ",u)
print("S= ",p)

#Ulesanne 6
t=float(input("\nSisesta tangitud kutuse liitrid:"))
k=float(input("Sisesta labitud km:"))
v=k/t*8
print("Keslmine kutusekulu 100km kohta - ",v)

#ulesanne 7
print("\nRulluisutaja keskmine kiirus on 29,9km/h")
v=29.9/16.667
print(v,"m labib rulluisutaja minutis") 

#ulesanne 8
a=float(input("Sisesta aja minutis: "))
v=a/60
t=a//60
m=v-t
v2=m*60
print("\nSisestus:",a,"\nVastus:",round(v),":",round(v2))

