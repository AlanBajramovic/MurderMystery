# Funktion för välkomstscenen
def welcome_scene():
    print("Välkommen till Murder Mystery!")  # Välkommen scen
    print("Du befinner dig i ett hus där du har 3 olika dörr")
    print("Du har bara tre liv. Förlorar du alla, är spelet över.")

# Funktion för dörruppgift 1
def door_task_1():
    print("Dörr 1: Hitta mördarens egenskaper!")
    traits = ["hårfärg", "längd", "typ av kropp"]

    # Loopa igenom och jämför svar med rätta svar
    for trait in traits:
        answer = input(f"Vad för {trait} har mördaren? ").lower()
        if answer == "brunett, lång, biffig":
            print("Fel svar! Du förlorar ett liv.")
            return True

        print("Rätt svar! Fortsätt vidare till nästa fråga.")

    print("Rätt svar! Du har klarat uppgifterna till dörr 1")
    return True

# Funktion för dörruppgift 2
def door_task_2():
    print("Dörr 2: Fälla! Du har triggat en fälla och förlorar ett liv.")
    print("Du måste starta om spelet.")
    return False

# Funktion för dörruppgift 3
def door_task_3():
    print("Dörr 3: Lösa tre uppgifter för att hitta mördaren.")
    tasks = ["Använde han pistol?", "Åkte han BIL eller MOPPED?", "Hade han YXA eller KNIV?"]

    correct_answers = tasks

    # Loopa igenom uppgifter och svar
    attempts = 3
    while attempts > 0 and tasks:
        task = tasks.pop(0)
        print(f"Uppgift: {task}")
        answer = input("Ditt svar (ja/nej):").lower()

        if answer == "ja":
            print("Rätt svar! Fortsätt till nästa fråga.")
        else:
            print("Fel svar! Du förlorar ett liv.")
            attempts = attempts - 1
        break

    attempts = 3
    while attempts > 0 and tasks:
        task = tasks.pop(0)
        print(f"Uppgift: {task}")
        answer = input("Ditt svar (bil/mopped):").lower()

        if answer == "bil":
            print("Rätt svar! Fortsätt till nästa fråga.")
        else:
            print("Fel svar! Du förlorar ett liv.")
            attempts = attempts - 1
        break

    attempts = 3
    while attempts > 0 and tasks:
        task = tasks.pop(0)
        print(f"Uppgift: {task}")
        answer = input("Ditt svar (yxa/kniv):").lower()

        if answer == "kniv":
            print("Rätt svar! Fortsätt till nästa fråga.")
        else:
            print("Fel svar! Du förlorar ett liv.")
            attempts = attempts - 1
        break
    # Loopa igenom uppgifter och svar för de två följande frågorna
    
    # Slutligen, bedöm om spelaren har klarat uppgifterna
    if attempts > 0:
        print("Bra jobbat! Du har hittat mördaren. Du får ett vapen!")
        return True
    else:
        print("Du förlorade alla dina liv. Spelet är över.")
        return False

# Huvudfunktionen
def main():
    welcome_scene()  # Välkommen scen till 3 olika dörr 

    while True:
        print("Du står framför tre dörrar.")
        answer = input("Vilken dörr väljer du? (1, 2 eller 3) ")

        # Hantera spelarens val och resultatet från dörruppgifterna
        if answer == "1":
            door_1_result = door_task_1()
            if door_1_result:
                print("Du klarade uppgifterna för dörr 1! Återgår till menyn.")
        elif answer == "2":
            door_2_result = door_task_2()
            if door_2_result:
                print("Fälla, du har blivit fångad av mördaren! Försök gärna spela om.")
                break
        elif answer == "3":
            door_3_result = door_task_3()
            if door_3_result: 
                print("Grattis, du har fångat mördaren och här får du ett vapen!")
                break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()  # Kod som strukturerar och organiserar Python-program
