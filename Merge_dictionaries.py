# WAP to merge dictionary using update () method

def Merge(dict1, dict2):
    return(dict1.update(dict2))

# main
dict1 = {'p': 15, 'a': 21}
dict2 = {'s': 24, 't': 4}
print(Merge(dict1, dict2))
print(dict1)
