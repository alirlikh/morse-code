MORSE_CODE_DICTIONARY = {'A': '.-', 'B': '-...',
                         'C': '-.-.', 'D': '-..', 'E': '.',
                         'F': '..-.', 'G': '--.', 'H': '....',
                         'I': '..', 'J': '.---', 'K': '-.-',
                         'L': '.-..', 'M': '--', 'N': '-.',
                         'O': '---', 'P': '.--.', 'Q': '--.-',
                         'R': '.-.', 'S': '...', 'T': '-',
                         'U': '..-', 'V': '...-', 'W': '.--',
                         'X': '-..-', 'Y': '-.--', 'Z': '--..',
                         '1': '.----', '2': '..---', '3': '...--',
                         '4': '....-', '5': '.....', '6': '-....',
                         '7': '--...', '8': '---..', '9': '----.',
                         '0': '-----', ', ': '--..--', '.': '.-.-.-',
                         '?': '..--..', '/': '-..-.', '-': '-....-',
                         '(': '-.--.', ')': '-.--.-', 'SOS': '...---...'}


def convertMorse(str):
    all_sentence = str.strip().upper()
    words = all_sentence.split(" ")
    convert = []
    for x in words:
        for i in x:
            if i in MORSE_CODE_DICTIONARY:
                convert.append(MORSE_CODE_DICTIONARY[i])

        if x != words[-1]:
            convert.append(" ")
    return " ".join(convert)


def decodeMorse(morse_code):
    all_sentence = morse_code.strip()
    words = all_sentence.split("   ")
    char = []
    convert = []
    for element in words:
        char.append(element.split(" "))
    for lists in char:
        for element in lists:
            for key, value in MORSE_CODE_DICTIONARY.items():
                if value == element:
                    convert.append(key)
        convert.append(" ")

    return "".join(convert).strip()


print("*" * 30, 'Hello', "*" * 30)
print("*" * 20, 'Welcome to Morse Convertor Program ', "*" * 30)

while True:
    print('  Choose your Operation: \n    1-String to Morse \n    2-Morse to String \n    3-Exit')
    print("      ?")
    operationInput = input()
    operation = ""
    res = ""
    if operationInput == "1":
        print('     Enter your String:')
        s = input()
        res = convertMorse(s)
        print('\n ')
        print('*' * 20, f"result: {res}   ", '*' * 20)
        print('\n \n \n')
    elif operationInput == "2":
        print('Enter your Morse code:')
        s = input()
        res = decodeMorse(s)
        print('*' * 20, f"result: {res} ", '*' * 20)
        print(' \n \n')
    elif operationInput == "3":
        print("*" * 30, 'Bye', "*" * 30)
        break
