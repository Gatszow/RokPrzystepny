#-*- coding: utf-8 -*-

from datetime import date

working = True
current_year = date.today().year


while working == True:

#Wprowadzanie roku i zamiana na integer
    year = input('Podaj rok, który cię interesuje:\n')
    try_1 = True
    while try_1 == True:
        try:
            year = int(year)
        except ValueError:
            year = input("Podaj rok jeszcze raz (Liczbowo):\n")
        if type(year) == int:
            try_1 = False
        else:
            pass

# Rok przystępny
    if year >= 0:
        if year%4 == 0:
            if year == 0:
                print("Rok narodzin CHRYSTUSA!!!! Jak najbardziej przystępny")
            elif year != 0:
                if year > current_year:
                    if current_year < year < current_year+4:
                        print("Rok {} jest przystępny, następny rok przystępny to {}".format(year, year+4))
                    else:
                        print("Rok {} jest przystępny".format(year))
                elif year < current_year:
                    print("Rok {} jest przystępny".format(year))
                elif current_year == year:
                    print("Rok {} w którym żyjemy, jest przystępny".format(year))

# Rok nieprzystępny
        elif year%4 != 0:
            print("Rok {} nie jest przystępny".format(year), end='')
            years_to_leap_year = year%4
            years = [None, 3, 2, 1]
            years_to_leap_year = years[years_to_leap_year]
            if current_year < year < current_year + 4:
                if years_to_leap_year == 1:
                    print(", został rok do następnego roku przystępnego")
                elif years_to_leap_year > 1:
                    print(", następny rok przystępny jest za {} lata (rok {})".format(years_to_leap_year, year+years_to_leap_year))
            else:
                print("")

# Nieprawidłowe wprowadzenie roku
    elif year < 0:
        print("Nieprawidłowy rok")

# Pytanie czy zakończyć program
    working = input("Czy chcesz zakończyć działanie programu? T/N\n")
    if working == "T":
        working = False
        print("PAPA")

    elif working == "F":
        working = True
        print("")


