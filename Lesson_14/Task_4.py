while
fib_iter = FibIterator(fib_list)
while True:
    try:
        print(next(fib_iter))
    except StopIteration:
        break