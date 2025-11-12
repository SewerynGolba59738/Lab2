

punkty = int(input("Podaj liczbę punktów:"))

if punkty > 80:
    print("Zaliczony egzamin")
elif punkty <= 80 and punkty >= 50:
    print("Możesz poprawić wynik")
else:
    print("Brak zaliczenia")
