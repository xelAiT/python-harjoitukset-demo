
käyttäjä = "python"
salasana = "rules"

max_yritykset = 5
yritykset = 0

while yritykset < max_yritykset:
    tunnus = input("Käyttäjätunnus: ")
    sana = input("Salasana: ")

    if tunnus == käyttäjä and sana == salasana:
        print("Tervetuloa")
        break

    else:
        print("Väärä käyttäjätunnus ja/tai salasana. Yritä uudelleen.")
        yritykset += 1

    if yritykset == max_yritykset:
        print("Pääsy evätty.")
        break