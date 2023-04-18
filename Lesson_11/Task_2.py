def reverse(*args):
    result = ""
    for word in args:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        result += reversed_word + " "
    return result[:-1]

words = input("Введите несколько слов через пробел: ").split()
print(reverse(*words))
