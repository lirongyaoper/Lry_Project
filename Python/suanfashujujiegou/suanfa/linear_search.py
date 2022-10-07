def linear_search(li,value):
    for ind,val in enumerate(li):
        if val==value:
            return ind
    else:
        return None

li=[63,55,87,744,44,12,96,36,45,71,85,51]
print(linear_search(li,71))