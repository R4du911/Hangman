import random


def random_line(fname):
    lines = open(fname).read().splitlines()
    s = random.choice(lines)
    p = s.split('/')
    return p[0].upper()


def zeichnung(var):
    if var == 0:
        f = open("life1.txt", "r")
        s = f.readline()
        while s != '':
            print(s, end='')
            s = f.readline()
        f.close()
    elif var == 1:
        f = open("life2.txt", "r")
        s = f.readline()
        while s != '':
            print(s, end='')
            s = f.readline()
        f.close()
    elif var == 2:
        f = open("life3.txt", "r")
        s = f.readline()
        while s != '':
            print(s, end='')
            s = f.readline()
        f.close()
    elif var == 3:
        f = open("life4.txt", "r")
        s = f.readline()
        while s != '':
            print(s, end='')
            s = f.readline()
        f.close()
    elif var == 4:
        f = open("life5.txt", "r")
        s = f.readline()
        while s != '':
            print(s, end='')
            s = f.readline()
        f.close()
    elif var == 5:
        f = open("life6.txt", "r")
        s = f.readline()
        while s != '':
            print(s, end='')
            s = f.readline()
        f.close()
    elif var == 6:
        f = open("death.txt", "r")
        s = f.readline()
        while s != '':
            print(s, end='')
            s = f.readline()
        f.close()
    print('\n')

def to_string(word,l):
    for x in range(len(word)):
        print('{} '.format(l[x]), end='')


def game(word):
    print(word)
    ctletter = 2
    x = 0
    zeichnung(x)
    l = []
    l.append(word[0])
    for x in range(1, len(word)-1):
        l.append('_')
    l.append(word[len(word)-1])
    to_string(word,l)
    x = 0

    while x < 6:
        gasit = 0
        print('\n')
        letter = input("Your input:")
        for el in range(len(word)):
            if word[el] == letter:
                l[el] = letter
                gasit = 1
                ctletter += 1
        if gasit == 0:
            print("NOTHING FOUND")
            x += 1
        zeichnung(x)
        to_string(word,l)
        print('\n')
        if ctletter == len(word):
            print("YOU WON")
            x = 7
    if x == 6:
        zeichnung(x)
        print("YOU LOST")
        print("THE WORD WAS: " + word)


def main():
    word = random_line('Dictionary.txt')
    game(word)


main()
