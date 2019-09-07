from random import randint

rand_num = randint(1, 100)

def zgaduj():
    try:
        num = int(input("Zgadnij liczbę: "))
    except ValueError:
        print("Podaj poprawną liczbę!")
        (zgaduj())
    if num > rand_num:
        print("Za dużo!")
        zgaduj()
    elif num < rand_num:
        if num < 0:
            print("Podaj liczbę większą od 0")
        else:
            print("Za mało!")
        zgaduj()
    else:
        print("Zgadłeś")

zgaduj()