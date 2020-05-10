phrase = "емуподушкипоправлятьпечальноподноситьлекарство"
alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "э", "ь", "э", "ю", "я"]

def buildOrder(alphabet, word):
    orderNumber = 1
    end = False
    order = []
    for i in range(len(word)):
        order.append(0)

    for i in alphabet:
        for j in range(len(word)):
            if i == word[j]:
                order[j] = orderNumber
                orderNumber += 1
                end = True
        if end:
            break

    for i in alphabet:
        for i in range(len(word)):
            if order[len(word) - i - 1] == 0:
                order[len(word) - i - 1] = orderNumber
                orderNumber += 1
    return order

def encryption(phrase, word, turn):
    script = []
    cipher = ""
    code = {}
    order = {}

    for i in word:
        script.append('')
    for i in range(len(phrase)):
        script[i % len(word)] += phrase[i]
    for i in range(len(script)):
        script[i] = script[i][0] + script[i][1] + script[i][2] + script[i][3] + script[i][4]

    for i in range(len(word)):
        code[script[i]] = word[i]
        order[turn[i]] = script[i]

    for i in range(1, len(word)+1):
        for j in range(len(turn)):
            if turn[j] == i:
                cipher += script[j]
        cipher += " "

    return [cipher, code, order]


def decryption(cipher, code, order):
    rightCipher = ""
    for i in buildOrder(alphabet, word):
        j = 0
        while j < len(cipher) - 1:
            cipherSymbol = ""
            cipherSymbol += cipher[j] + cipher[j + 1] + cipher[j + 2] + cipher[j + 3] + cipher[j + 4]
            if order[i] == cipherSymbol:
                rightCipher += cipherSymbol + " "
                break
            else:
                j += 6

    rightWord = ""
    rightLetters = rightCipher.split()
    for i in rightLetters:
        rightWord += code[i]

    return rightWord

word = (input("Введите слово: ")).lower()

turn = buildOrder(alphabet, word)
wordWork = encryption(phrase, word, turn)
cipher = wordWork[0]
code = wordWork[1]
order = wordWork[2]

wordToPrint = ""
orderToPrint = ""
for i in range(len(word)):
    wordToPrint += word[i] + " "
    orderToPrint += str(turn[i]) + " "

print(wordToPrint)
print(orderToPrint)
print()
for i in range(5):
    cipherLine = ""
    j = i
    while j < len(cipher):
        cipherLine += cipher[j] + " "
        j += 6
    print(cipherLine)
print()
print("Зашифрованное слово: " + decryption(cipher, code, order))