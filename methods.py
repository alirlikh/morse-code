from constants import MORSE_CODE_DICTIONARY


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
