def filter_list(l):
    g = []
    for i in l:
        if type(i) == int:
            g.append(i)
            
    return g