def slicer(tupl, elem):
    if elem in tupl:
        if tupl.count(elem) > 1:
            first = tupl.index(elem)
            second = tupl.index(elem, first + 1) + 1
            return tupl[first:second]
        else:
            return tupl[tupl.index(elem):]
    else:
        return ()