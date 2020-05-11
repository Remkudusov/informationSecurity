# -*- coding: utf8 -*-
# в переменную phrase нужно написать свой вариант ключевой фразы
phrase = "емуподушкипоправлятьпечальноподноситьлекарство"
fullAlphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ь", "э", "ю", "я"]
excessSymbols = ["!", "?", "."]

def buildPolibianSquare(phrase, fullAlphabet, excessSymbols):
    notAlphabet = []
    alphabet = []

    for i in phrase:
        flag = True
        for j in alphabet:
            if i == j:
                flag -= 1
                break
        if flag:
            alphabet.append(i)

    for i in fullAlphabet:
        flag = True
        for j in alphabet:
            if i == j:
                flag -= 1
                break
        if flag:
            notAlphabet.append(i)

    alphabet += notAlphabet

    polibianSquare = []
    for i in range(6):
        string = []
        for j in range(6):
            letter = i * 6 + j
            if letter < len(alphabet):
                string.append(alphabet[letter])
            else:
                string.append(excessSymbols[letter - len(alphabet)])
        polibianSquare.append(string)
    return polibianSquare

def encrypt(word, polibianSquare):
    stringCoordinates = []
    columnCoordinates = []
    cipher = ""

    for letter in word:
        for i in range(6):
            for j in range(6):
                if letter == polibianSquare[i][j]:
                    stringCoordinates.append(i)
                    columnCoordinates.append(j)

    allCoordinates = stringCoordinates + columnCoordinates

    i = 0
    stringCoordinates = []
    columnCoordinates = []
    while i < len(allCoordinates):
        stringCoordinates.append(allCoordinates[i])
        columnCoordinates.append(allCoordinates[i + 1])
        i += 2

    for i in range(len(stringCoordinates)):
        cipher += polibianSquare[stringCoordinates[i]][columnCoordinates[i]]

    return cipher

def decrypt(cipher, polibianSquare):
    stringCoordinates = []
    columnCoordinates = []
    allCoordinates = []
    decryption = ""

    for letter in cipher:
        for i in range(len(polibianSquare)):
            for j in range(len(polibianSquare[i])):
                if letter == polibianSquare[i][j]:
                    stringCoordinates.append(i)
                    columnCoordinates.append(j)

    for i in range(len(stringCoordinates)):
        allCoordinates.append(stringCoordinates[i])
        allCoordinates.append(columnCoordinates[i])

    stringCoordinates = []
    columnCoordinates = []

    #print(len(allCoordinates))
    #print(int((len(allCoordinates))/2))
    for i in range(int((len(allCoordinates))/2)):
        stringCoordinates.append(allCoordinates[i])
        columnCoordinates.append(allCoordinates[i + int((len(allCoordinates))/2)])

    for i in range(len(stringCoordinates)):
        decryption += polibianSquare[stringCoordinates[i]][columnCoordinates[i]]

    return decryption

word = str(input("Введите слово: "))

polibianSquare = buildPolibianSquare(phrase, fullAlphabet, excessSymbols)
for i in range(len(polibianSquare)):
    string = ""
    for j in polibianSquare[i]:
        string += j + " "
    print(string.strip())

print()
cipher = encrypt(word, polibianSquare)
print(encrypt(word, polibianSquare))
print()
print(decrypt(cipher, polibianSquare))
