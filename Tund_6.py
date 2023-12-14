
# 7 Sorteerimine
from random import*
num=randint(2,20)
num_list=[]
for i in range(num):
    num_list.append(randint(-100,100))
print("\nEsimene list - ",num_list)
print()
for element in num_list:
    if element<0:
        n=num_list.index(element)
        num_list[n]=abs(element)
num_list.sort()
print("Absolut list - ",num_list)
num_list.sort(reverse=True)
print("Reverse absolut list - ",num_list)



# 6 Mõtetu numbrid
from random import*
spisok=randint(2,20)
num_list=[]
for i in range(spisok):
    num_list.append(randint(0,100))
print("\n",num_list)
print()
max_n=max(num_list)
print("Suurem number -", max_n)
kokku=len(num_list)
print("Meil on ",kokku," numbrid")
new=print("Uus number - ",round(max_n/kokku,0))
new=round(max_n/kokku,0)
n=num_list.index(max_n)
print(n+1)
num_list.pop(n)
num_list.insert(n, new)
print(num_list)



# 5 Vahetus
from random import*
kokku=randint(2,20)
num_list=[]
for i in range(kokku):
    num_list.append(randint(-100,100))
print("\n",num_list)
print()
while True:
    try:
        kogus=int(input("Mitu positsiooni vahetada?"))
        if kogus<=kokku/2:
            break
    except:
        print("Proovi uuesti!")
for i in range(0, kogus,1):
    x_tmp=num_list[i]
    num_list[i]=num_list[(len(num_list)-i)-1]
    num_list[(len(num_list)-i)-1] = x_tmp
print("\n", num_list)



# 4 postiindeks
indexid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve", "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa",'Tartu linn','Tartumaa, Põlvamaa, Võrumaa, Valgamaa','Viljandimaa, Jarvamaa, Harjumaa, Raplamaa','Parnumaa','Läänemaa, Hiiumaa, Saaremaa']
while True:
    try: 
        index=int(input("Sisesta postiindeks: "))
        if len(str(index))==5: #"12345
            break
    except:
        print("Viga!")
print("Indeksi analüüs")
index_list=list(str(index))
s1=int(index_list[0]) # 1 -> 0 Tallinn
print("Index {0} kuulub {1} piirkonnale".format(index,indexid[s1-1]))
