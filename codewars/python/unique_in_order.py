test1 = "AAAABBBCCDAABBB"
test2 = "ABBCcAD"
test3 = [1,2,2,3,3]
tests = [test1, test2, test3]


def unique_in_order(iterable):
    head = iterable[0]
    tail = iterable[1:]

    unique = []
    for item in tail:
        if head != item:
            unique.append(head)
            head = item

    unique.append(head)
    return unique



from itertools import groupby

def unique_in_order(iterable):
    return [k for k, g in groupby(iterable)]