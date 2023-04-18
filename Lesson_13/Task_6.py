def alphabet():
    for i in range(97, 123):
        print(chr(i), i-96)
alphabet()

def alphabet():
    alph_dict = {}
    for i in range(97, 123):
        alph_dict[i-96] = chr(i)
    return alph_dict
print(alphabet())
