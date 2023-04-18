def alphabet():
    for letter in range(ord('a'), ord('z')+1):
        yield chr(letter)

while:
a = alphabet()
while True:
    try:
        print(next(a))
    except StopIteration:
        break