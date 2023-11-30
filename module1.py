# Lesson 3 

from math import *
from random import *

#Vigade otsing 2


print("*** MANGUD NUMBRIDEGA ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1: 
	try:
		a = abs(int(input("Sisesta taisarv => ")))    # lisatud ))
		break
	except ValueError:
		 print("See ei ole taisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
	print("Nulliga pole motet midagi ette votta")
else:
	#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	print("Maarake, kui palju paaris ja mitu paaritu numbrit on arvus")
	print()
	c=b=a   # == -> =
	paaris =0
	paaritu = 0
	while b > 0:    # ; -> :
			if b % 2 == 0:  # = -> ==
				paaris =+ 1
			else:
				paaritu =+ 1
			b = b // 10    # b oli vales kohas
	
	print("Paaris arvud:",paaris) # lisatud ,
	print("Paaritud arvud:",paaritu)
	print()
		#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("*Tagurda* sisestatud number")
print() 
b=0
while a > 0:  #lisatud :
  number = a % 10
  a = a // 10
  b = b * 10
  b =+number
print("*umberpooratud* number", b) 
print()
		#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Siracuse hupoteesi testimine") # (( -> (
print()

if c%2== 0:  # = -> ==
	print(c,"- paarisarv. Jagage 2-ga.")	
else:
	print(c,"- paaritu number. Korrutage 3-ga, lisage 1 ja jagage 2-ga.")
	while c!= 1:
			if c % 2 == 0:  # = -> ==
				c == c / 2
			else:
				c == (3*c + 1) / 2
			print(c, end=",")  # lisatud ","
print()
print("Hupotees on toene")   # '' -> "
print()


# Ulesanned 10tk

#12
n=randint(2,10)
m=randint(1,10) #n-1
summa=0
print("masinad: ",n)
print("tunnid: ",m)
for t in range(n-1):
	m=(m/6)*7
	summa+=m
	print(m)
print("Kokku masinad tootasid: ", summa, "t")
	

#8
for x in range(1,21):
	print(x,"cm =",x*2.5,"inch")


#7
print()
a=int(input("Sisesta a: "))
b=int(input("Sisesta b: "))
k=int(input("Sisesat k: "))
for x in range(a,b):
	if x%k==0:
		print(x)



#13
print()
summa=0
count=0
for x in range(100,1000):
	if x%7==0:
		summa+=7
		count+=1
print(summa)
print(count)



#29
print()
for i in range(9):
	for x in range(9):
		if x==0 or i==x:
			print("x",end=" ")
		else:
			print("0",end=" ")
	print()


#15 
print()
for y in range(10):
	for x in range(10):
		print(x,end=" ")
	print()


#4
print()
for x in range(10,21):
	print(x**2, end=";",)


#5
number=int(input("\nSisesta A: "))
summa=0
for i in range (-1,number-1,-1):
	if number<0:
				summa+= i
print(summa)


#3
print()
p=1
lause=""
for x in range(8):
	A=float(input("{0}. samm\nSisesta A: ".format(x+1)))
	if A>0:
		p*=A
		lause=lause+str(A)+"*"    # 4to b9 pokaz9valo 4to pereumnozaem
print(lause[:-1],"=",p)     #  [:-1] - ubratj poslednii simvol


#2
print()
number=int(input("Sisesta A: "))
summa=0
for i in range (number+1):
	if number>0:
				summa+= i
print(summa)

#2.2
print()
summa=0
number=int(input("Sisesta A: "))
for i in range(1,number+1,1):
	summa+=i
print("Summa: {0}".format(summa))


# 1
print()
t=0
for x in range(15):
	A=float(input("Sisesta A: "))
	if A.is_integer():   # 5.0==True; 5.5=False
		t+=1
print(t)




#Naide

#Variant 1 - for __ in range
for x in range(1,11):                           #(10)
	R=float(input("{0}R: ".format(x)))          #format(x+1)
	if R>0:
		S=pi*R**2
	else:
		S="R peab > kui 0 olema"
	print("S={0}".format(S))


# Variant 2 - while True
x=0
while True:
	x+=1
	R=float(input("{0}R: ".format(x)))          
	if R>0:
		S=pi*R**2
	else:
		S="R peab > kui 0 olema"
	print("S={0}".format(S))
	if x==10:
		break


# Variant 3 - x<10
x=0
while x<10:
	x+=1
	R=float(input("{0}R: ".format(x)))          
	if R>0:
		S=pi*R**2
	else:
		S="R peab > kui 0 olema"
	print("S={0}".format(S))
	

x=0
while True:
	R=float(input("{0}R: ".format(x)))          
	if R>0:
		S=pi*R**2
		x+=1
	else:
		S="R peab > kui 0 olema"
	print("S={0}".format(S))
	if x==10:
		break

