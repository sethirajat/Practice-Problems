'''
Q-8.3
Write a method that returns all subsets of a set.

'''

def all_subsets(inp, idx):
    if idx >= len(inp):
        return None

    if idx == len(inp) - 1:
        return [[inp[idx]]]

    subs = all_subsets(inp,idx+1)
    res = []
    res.extend(subs)
    for sub in subs:
        elem = sub + [inp[idx]]
        res.append(elem)

    #res.extend(subs)
    res.append([inp[idx]])

    return res

set1 = ['a','b','c','d']

print all_subsets(set1, 0)
