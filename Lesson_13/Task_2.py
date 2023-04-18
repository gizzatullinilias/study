def normalize_names(names):
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    for name in names:
        name = ''.join([char for char in name if char in valid_chars])
        name = name.capitalize()
        result.append(name)
    return result

s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
normalized_s = normalize_names(s)
print(normalized_s) # ['Антон', 'Наталья', 'Никита', 'Мария', 'Сергей', 'Владимир', 'Павел']

