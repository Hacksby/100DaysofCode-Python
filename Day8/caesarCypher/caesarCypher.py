import art
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(art.logo)
print("Welcome to this Caesar encryption tool!\n")
keepGoing = True

while keepGoing:
    option = int(input("Write the number of the desired option:\n1. Encoding\n2. Decoding\n"))
    text = input("Write your text: \n")
    shift = int(input("Enter a number of positions: \n"))
    finalText = ""
    optionName = "encode"
    if option == 2:
        shift *= -1
        optionName = "decode"
    for letter in text:
        position = alphabet.index(letter)
        cipherPosition = position + shift
        while cipherPosition > 25:
            cipherPosition -= 26
        while cipherPosition < 0:
            cipherPosition += 26
        finalText += alphabet[cipherPosition]
    print(f"The {optionName}d text is: {finalText}")

    endingSelection = int(input("Do you want run the program again?:\n 1. Yes\n 2. No\n"))

    if endingSelection == 2:
        keepGoing = False
        print("Thanks for using caesarCypher!")
