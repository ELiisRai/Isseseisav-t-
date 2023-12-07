#Ulesanne 2
names = []
n1=input("Esimene nimi: ")
n2=input("Teine nimi: ")
n3=input("Kolmas nimi: ")
n4=input("Neljas nimi: ")
n5=input("Viimane nimi: ")
names.append(n1)
names.append(n2)
names.append(n3)
names.append(n4)
names.append(n5)
names.sort()
print(names, "Viimane nimi oli: ",n5)

change=input("Kas sa soovid midagi vahetada? Jah või ei?\n")
if change=="jah":
    vana=input("Milline nimi sa soovid vahetada? (1,2,3,4,5)\n")
    uus=input("Sisesta uus nimi: ")
    names[vana]=uus
else:
    pass
print(names)

#set() pereberet vse 4to estj i vidast v odnom ekzempljare

#Ulesanne 1

import string

text=input("\n Sisesta tekst: " )
count_a=0
count_b=0
count_z=0
count_num=0
text_list=list(text)
k=len(text_list)
a="a","e","u","i","o"
a_list=list(a)
z=string.punctuation

for letter in text_list:
    if letter in a_list:
        count_a+=1
    elif letter in z:
        count_z+=1
    elif letter.isdigit():
        count_num+=1
    else:
        count_b+=1
print("Vookali: ",count_a)
print("Konsonanti: ",count_b)
print("Tühikud ja kirjavahemärgid: ",count_z)
print("Numbrid: ", count_num)



text=input("Sisesta tekst: ")  #text->["t","e"...] num ->[1,2,3]
text_list=list(text)
k=len(text_list)
if text.isdigit(): 
    for t in range(k):      
        num=int(text_list[t])
        text_list.pop(t) #=remove
        text_list.insert(t,num)
     
    summa=0
    for e in text_list:
        summa+=e
    print("Summa: ",summa)        
print(text_list)
 
e=input("Element: ") #str tip dann9h
try:
    if e.isalpha():
        indeks=text_list.index(e)
    else:
        indeks=text_list.index(int(e))
    print("Element: {0} on {1} positsioonil".format(e,indeks+1))  #+1 4tob normalno otobrazalos, na4inaja s 1
except:
    print("Element puudub")

