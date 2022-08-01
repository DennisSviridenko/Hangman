import random

words = ["Hallo", "moin", "lol", "jo", "z"]
show = []
hidden = []
hide = []
versuche = 0



def setup():
    x = random.choice(words)
    for i in x:
        hidden.append(i)
        hide.append(0)

def main():
    setup()
    print(hidden)
    print(hide)
























if __name__ == '__main__':
    main()
