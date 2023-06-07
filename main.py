import random

def wisielec():
    slowa = ["papież", "banan", "karmazyn", "tasiemiec", "niedźwiedzica", "usprawiedliwienie", "dźwiękonaśladownictwo", "marzenie", "spoceniec", "przypadłość", "koncentracja", "szczepionka", "szaszłyk", "chłopiec", "huragan", "przewodnik", "darmozjad", "mrówkojad", "orzechy", "kobieta", "tabernakulum", "użytkownik", "hostia", "elementarność", "ekspres", "smarowidło", "madagaskar", "huncwot", "kazjerka", "pierwiatek", "elokwencja", "dominika", "farmazon", "źdźbło", "komputer", "kabaczek", "sprzedawca", "komendant", "donosiciel", "deformacja", "konsternacja", "kuba", "zapiekanka", "laska", "żywioł", "konsternacja", "cockerspaniel", "niedźwiedź", "wirtualizacja", "maciek", "butelka", "frytki", "lodówka", "alkohol", "garnek", "szklanki", "młodzieniec", "krzesło", "marakuja", "czajnik", "magdalena", "jamnik", "babcia", "echolokacja", "lokaj", "leokadia", "szafka", "kurtka", "bluza", "chleb", "masło", "cytryna", "płachta", "płaszcz", "nędza", "cukier", "kawa", "matryca", "pokrowiec", "krowa", "świnia", "nosorożec", "monitor", "kebab", "dżem", "grzyby", "widelec", "łyżka", "wisielec", "hasło", "batonik", "wiosło", "łódka", "jezioro", "medalion", "wiedźmin", "głód", "igor", "koń", "olej", "telefon", "miska", "lampka", "stupki", "wędliny", "maskarada", "subiektywność", "kadzidło", "befsztyk", "pendrive", "szwecja", "malediwy", "sebastian", "krzysztof", "rosja", "kanada", "miecz", "czechy", "siekiera", "biurko", "pióro", "ręcznik", "gąsienica", "środowisko", "żółądź", "owca", "matematyka", "informatyka", "programowanie", "szermierka", "wychowanie", "kaloryfer", "mięso", "magnez", "kontroler", "przełącznik", "ładowarka", "realizm", "język", "kanapka", "szachy", "kiełbasa", "szynka", "kurczak", "kapeć", "ziemniaki", "pomidor", "deprywatyzacja", "żaba", "recydywista", "uzurpator", "ambiwertyk", "ambiwalencja", "studentka", "zimbabwe", "średniowiecze", "teraźniejszość", "konwalescencja", "wybrzeże", "gryzmolić", "schaboszczak", "nieboszczyk", "doświadczenie", "dewastacja", "łokieć", "kolana", "klient", "placek", "dynia", "wrzątek", "słodycze", "permutacja", "iteracja", "michał", "sokół", "szef", "umysł", "aktor", "artysta", "biuro", "matrymonium", "żelazko", "deska", "słownik", "strona", "internet", "podstawa", "folder", "cudzysłów", "miś", "kołdra", "pościel", "poduszka", "gruszka", "ananas", "drwal", "górnik", "kilof", "łopata", "bóbr", "parapet", "parasol", "hiperwentylacja"]
    wybrane_slowo = random.choice(slowa)
    odgadniete_litery = []
    zycia = 10

    print("Witaj w grze Wisielec!\nSpróbuj odgadnąć hasło zanim człowiek zostanie powieszony")

    while True:
        ukryte_slowo = ""
        for litera in wybrane_slowo:
            if litera in odgadniete_litery:
                ukryte_slowo += litera
            else:
                ukryte_slowo += "_"

        print("Hasło: " + ukryte_slowo)
        print("Wpisane litery:", odgadniete_litery)
        print("Liczba prób:", zycia)

        if zycia == 9:
            print("\n\n\n\n\n\n=========")
        elif zycia == 8:
            print("      +\n      |\n      |\n      |\n      |\n      |\n=========")
        elif zycia == 7:
            print("  +---+\n      |\n      |\n      |\n      |\n      |\n=========")
        elif zycia == 6:
            print("  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========")
        elif zycia == 5:
            print("  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========")
        elif zycia == 4:
            print("  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========")
        elif zycia == 3:
            print("  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========")
        elif zycia == 2:
            print("  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========")
        elif zycia == 1:
            print("  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========")


        if ukryte_slowo == wybrane_slowo:
            print("Gratulacje! Odgadłeś hasło: " + wybrane_slowo)
            break
        elif zycia == 0:
            print("  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\nPrzegrałeś! Hasło to: " + wybrane_slowo)
            break

        zgadywane_slowo = input("Podaj literę lub wpisz \"odgadnij\", aby spróbować zgadnąć całe hasło: ").lower()

        if zgadywane_slowo.lower() == "odgadnij":
            calkowite_slowo = input("Podaj całe hasło: ").lower()
            if calkowite_slowo == wybrane_slowo:
                print("Wygrałeś! Hasło to: " + wybrane_slowo)
                break
            else:
                print("  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\nNiestety nie udało ci się odgadnąć hasła :( Hasło brzmiało: " + wybrane_slowo)
                break
        elif len(zgadywane_slowo) != 1 or not zgadywane_slowo.isalpha():
            print("To nie jest pojedyncza litera, spróbuj jeszcze raz: ")
            continue

        if zgadywane_slowo in odgadniete_litery:
            print("Ta litera została już wpisana, podaj inną literę: ")
        elif zgadywane_slowo in wybrane_slowo:
            odgadniete_litery += zgadywane_slowo
        else:
            print("\nNie ma takiej litery w haśle\n")
            odgadniete_litery += zgadywane_slowo
            zycia -= 1

wisielec()

