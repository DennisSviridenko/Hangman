import random

words = ["Hallo", "moin", "lol", "jo", "z"]
show = []
hidden = []
hide = []
versuche = 12345666876876876876


def setup(word):
    word = random.choice(words)
    for i in word:
        hidden.append(i)
        hide.append(0)

def printer():
    x = 0
    for i in hidden:
        if hide[x] == 0:
            # if x == word.length():
            print("_", end=" ")
        elif hide[x] == 1:
            print(i, end=" ")







def main():
    setup()
    print(print(word))
    print(len(word))
























if __name__ == '__main__':
    main()
