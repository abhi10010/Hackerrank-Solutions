def print_rangoli(size):
    
    import string
    alpha = string.ascii_lowercase

    L = []

    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    
    print('\n'.join(L[:0:-1]+L))
