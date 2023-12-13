import random
print("Привет! Давай сыграем в камень-ножницы-бумага")
while True:
    user=input("Выбери - камень/ножницы/бумага\n")
    v=["камень","ножницы","бумага"]
    komp=random.choice(v)
    print("Вы выбрали - ",user,"\nКомпьютер выбрал - ",komp)
    user_p=0
    komp_p=0
    if user==komp:
        print(f"Оба выбрали {user}. Ничья!")
        user_p=1
        komp_p=1
    elif user == "камень":
        if komp == "ножницы":
            print("Камень бьет ножницы! Вы победили!")
            user_p=1
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
            komp_p=1
    elif user == "бумага":
        if komp == "камень":
            print("Бумага оборачивает камень! Вы победили!")
            user_p=1
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
            komp_p=1
    elif user == "ножницы":
        if komp == "бумага":
            print("Ножницы режут бумагу! Вы победили!")
            user_p=1
        else:
            print("Камень бьет ножницы! Вы проиграли.")
            komp_p=1
    
    print(f"Счет - {user_p}:{komp_p}")
    veel=input ("Хочешь сыграть еще? Если хочешь закончить напиши - ESC  : ")
    if veel == "ESC":
        print(f"Игра закончена! Счет {user_p}:{komp_p}")
        break