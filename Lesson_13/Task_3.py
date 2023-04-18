def honest(s):
    result = []
    for i in s:
        if i % 2 == 0:
            result.append(i)
    return result

s = list(range(21))
even_numbers = honest(s)
print(even_numbers) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
