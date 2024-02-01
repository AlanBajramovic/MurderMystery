# Funktion för välkomstscenen
def välkomstscen():
    print("Välkommen till Murder Mystery!")  # Välkommen scen
    print("Du befinner dig i ett hus där du har 3 olika dörr")
    print("Det är endast tre liv som gäller! Förlorar du alla, är spelet över.")

# Funktion för dörruppgift 1
def dörruppgift_1():
    print("Dörr 1: Hitta mördarens egenskaper!")
    uppgifter = ["Var han brunnet?", "Var han lång eller kort?", "Var han biffig eller skinny?", ]

    # Loopa igenom och jämför svar med rätta svar
    försök = 3
    while försök > 0 and uppgifter:
        uppgift = uppgifter.pop(0)
        print(f"Uppgift: {uppgift}")
        svar = input("Ditt svar (ja/nej):").lower()

        if svar == "ja":
            print("Rätt svar! Fortsätt till nästa fråga.")
        else:
            print("Fel svar! Du förlorar ett liv.")
            försök = försök - 1
        break

    försök = 3
    while försök > 0 and uppgifter:
        uppgift = uppgifter.pop(0)
        print(f"Uppgift: {uppgift}")
        svar = input("Ditt svar (lång/kort):").lower()

        if svar == "lång":
            print("Rätt svar! Fortsätt till nästa fråga.")
        else:
            print("Fel svar! Du förlorar ett liv.")
            försök = försök - 1
        break

    försök = 3
    while försök > 0 and uppgifter:
        uppgift = uppgifter.pop(0)
        print(f"Uppgift: {uppgift}")
        svar = input("Ditt svar (biffig/skinny):").lower()

        if svar == "biffig":
            print("Rätt svar. Du har klarat uppgifter till dörr 1 återgår till menyn!")
        else:
            print("Fel svar! Du förlorar ett liv.")
            försök = försök - 1
        break

# Funktion för dörruppgift 2
def dörruppgift_2():
    print("Dörr 2: Fälla! Du har triggat en fälla och förlorar ett liv.")
    print("Du måste starta om spelet.")
    return False

# Funktion för dörruppgift 3
def dörruppgift_3():
    print("DÖRR 3: Lös tre uppgifter för att hitta mördaren.")
    uppgifter = ["Använde han pistol?", "Åkte han bil eller mopped?", "Hade han yxa eller kniv?"]

    rätta_svar = uppgifter

    # Loopa igenom uppgifter och svar
    försök = 3
    while försök > 0 and uppgifter:
        uppgift = uppgifter.pop(0)
        print(f"Uppgift: {uppgift}")
        svar = input("Ditt svar (ja/nej):").lower()

        if svar == "ja":
            print("Rätt svar! Fortsätt till nästa fråga.")
        else:
            print("Fel svar! Du förlorar ett liv.")
            försök = försök - 1
        break

    försök = 3
    while försök > 0 and uppgifter:
        uppgift = uppgifter.pop(0)
        print(f"Uppgift: {uppgift}")
        svar = input("Ditt svar (bil/mopped):").lower()

        if svar == "bil":
            print("Rätt svar! Fortsätt till nästa fråga.")
        else:
            print("Fel svar! Du förlorar ett liv.")
            försök = försök - 1
        break

    # Återställ uppgifter för nästa fråga
    uppgifter = list(rätta_svar)

    försök = 3
    while försök > 0 and uppgifter:
        uppgift = uppgifter.pop(0)
        print(f"Uppgift: {uppgift}")
        svar = input("Ditt svar (yxa/kniv):").lower()
        if svar == "kniv":
            print("Rätt svar, får uppgifter för att hitta mördarens plats..")
        else:
            print("Fel svar! Du förlorar ett liv.")
            försök = försök - 1
        break
    # Bedöm om spelaren har klarat uppgifterna
    if försök > 2:
        print("Bra jobbat! Du har hittat mördaren. Du får ett vapen!")
        return True
    else:
        print("Du förlorade alla dina liv. Spelet är över.")
        return False
    # Slutligen, bedöm om spelaren har klarat uppgifterna

# Huvudfunktionen
def huvud():
    välkomstscen()  # Välkommen scen till 3 olika dörr 

    while True:
        print("Du står framför tre dörrar.")
        svar = input("Vilken dörr väljer du? (1, 2 eller 3) ")

        # Hantera spelarens val och resultatet från dörruppgifterna
        if svar == "1":
            dörr_1_resultat = dörruppgift_1()
            if dörr_1_resultat:
                print("Du klarade uppgifterna för dörr 1! Återgår till menyn.")
        elif svar == "2":
            dörr_2_resultat = dörruppgift_2()
            if dörr_2_resultat:
                print("Fälla, du har blivit fångad av mördaren! Försök gärna spela om.")
                break
        elif svar == "3":
            dörr_3_resultat = dörruppgift_3()
            if dörr_3_resultat: 
                print("Grattis, du har klarat av spelet, tack för att du spelar
