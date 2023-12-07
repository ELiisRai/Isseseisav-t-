
from random import*
from math import*
import sys

correct_answers=0
opl= [ "+","-","*","/","**" ]

dif=0
print("Kirjuta END kui sa tahad lõppetada")
while dif not in [1,2,3]:
    dif=int(input("Vali mis tase sa soovid(1,2 või 3): "))
    if dif =="END":
        sys.exit()
qs=str(input("Kui palju küsimused sa soovid? "))
if qs=="END":
    sys.exit()

qs=int(qs)

for i in range(int(qs)):
    correct=None
    opn=randint(1,4)
    op=opl[opn]
    num1=randint(1,dif*10)
    num2=randint(1,dif*10)
    num3=randint(1,dif*10)
    num4=randint(1,4)

    if op=="+":
        correct=num1+num2
        print(f"{num1}{op}{num2}")
    elif op=="-":
        correct=num1-num2
        print(f"{num1}{op}{num2}")
    elif op=="/":
        correct=round(num1/num2, 2)
        print(f"{num1}{op}{num2}")
    elif op=="*":
        correct=num1*num2
        print(f"{num1}{op}{num2}")
    elif op=="**":
        correct=num3**num4
        print(f"{num3}{op}{num4}")
    v=float(input("Sisesta oma vastus(max 2 numbrit pärast koma): "))
    if v=="END":
        print("Head aega!")
        sys.exit
    elif v==correct:
        correct_answers+=1
        print("Õige!")
    else:
        print(f"Vale! Vastus {correct}")

percentage=(correct_answers / qs) * 100
for i in range(5):
    print()
if percentage<60:
    print("Hinne - 2")
elif percentage<75:
    print(" Hinne - 3")
elif percentage<90:
    print("Hinne - 4")
else:
    print("Hinne - 5! Tubli!")

