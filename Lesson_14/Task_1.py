# опустошение генератора с помощью цикла
def countdown():
    for i in range(10, -1, -1):
        yield i

c = countdown()
for i in c:
    print(i)

#опустошение генератора с помощью next()
def countdown():
    for i in range(10, -1, -1):
        yield i

c = countdown()
while True:
    try:
        print(next(c))
    except:
        break