def del_from_tuple(tupl, elem):
    lst = list(tupl)
    if elem in tupl:
        lst.remove(elem)
    return tuple(lst)