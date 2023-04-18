import string

alphabet = list(string.ascii_lowercase)
dictionary = {i + 1: alphabet[i] for i in range(23)}

print(dictionary)