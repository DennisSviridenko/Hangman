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
            if x < (len(word) - 1):
                print(i, end=" ")
        
        x += 1

def input_controll():
    global versuche
    versuche = 6876876876876876876
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
                    break
            
                z += 1
        else:
            versuche -= 1
            print("Leider Falsch, noch ", versuche, " Versuche!!!")            



def win():
    pass


def main():
    setup()
    while True:
        printer()
        input_controll()
    
        if versuche == 0: 
            print("Du hast verloren!!!")
            break





if __name__ == '__main__':
    main()
