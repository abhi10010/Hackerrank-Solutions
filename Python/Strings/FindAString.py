def count_substring(string, sub_string):
    
    count=0
    x = len(sub_string)
    
    for i in range(len(string)):
        check = string[i:i+x]
        
        if check==sub_string:
            count+=1
    
    return count

