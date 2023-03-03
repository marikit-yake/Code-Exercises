keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]

def createDict(keys, values):
    while len(keys) > len(values):
        values.append(None)

    return dict(zip(keys, values))

print(createDict(keys, values))