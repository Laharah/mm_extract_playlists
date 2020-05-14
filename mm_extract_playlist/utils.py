from collections import defaultdict

def groupby(iterable, key=lambda it: it):
    'Return a dic whose keys are key(it) and whose values are elements of iterable with that key.'
    dic = defaultdict(list)
    for it in iterable:
        dic[key(it)].append(it)
    return dic

