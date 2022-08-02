import random

words = ["Hallo", "moin", "lol", "jo", "z"]
hidden = []
hide = []



def setup():
    global word
    word = random.choice(words)
    for i in word:
        hidden.append(i)
        hide.append(0)


def printer():
    x = 0
    for i in hidden:
        if hide[x] == 0:
            if x == (len(word) - 1):
                print("_")
            elif x < (len(word) - 1):
                print("_", end=" ")
        elif hide[x] == 1:
            if x == (len(word) - 1):
                print(i)
            elif x < (len(word) - 1):
                print(i, end=" ")
        
        x += 1

def input_controll(versuche):
    x = input(">>> ")
    z = 0
    if len(x) > 1:
        if x == word:
            win()
        else:
            versuche -= 1
            print("Leider Falsch, noch ", versuche, " Versuche!!!")
    else:
        if x in hidden:
            for i in hidden:
                if i == x:
                    hide[z] = 1

                z += 1
        else:
            versuche -= 1
            print("Leider Falsch, noch ", versuche, " Versuche!!!")            

    z = 0
    for i in hide:
        if i == 1:
            z += 1
        
        if z == len(word):
            win()
    
    main(versuche)



def win():
    print(f"Du hast Gewonnen das Lösungswort war {word}")
    exit()


def main(vrsuche):
    if vrsuche <= 0: 
        print(f"Du hast verloren, das Lösungswort war {word}")
        exit()
    printer()
    input_controll(vrsuche)
        


if __name__ == '__main__':
    versuche = 8
    setup()
    main(versuche)