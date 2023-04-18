def tpl_sort(data):
    if all(isinstance(x, int) for x in data):
        return tuple(sorted(data))
    else:
        return data


