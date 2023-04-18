def cesar(string):
    result = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + 3 - 65) % 26 + 65)
            else:
                result += chr((ord(char) + 3 - 97) % 26 + 97)
        else:
            result += char
    return result

string = input("Введите строку для шифрования: ")
print("Зашифрованная строка: ", cesar(string))
