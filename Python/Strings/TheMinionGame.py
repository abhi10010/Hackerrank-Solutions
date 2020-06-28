def minion_game(string):
    
    k, s = 0, 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(len(string)):
        
        if string[i] not in vowels:
            s += 1
            s = s + len(string) - (i + 1)
        else:
            k += 1
            k = k + len(string) - (i + 1)
    
    if s > k:
        print('Stuart', s)
    elif s == k:
        print('Draw')
    else:
        print('Kevin', k)
