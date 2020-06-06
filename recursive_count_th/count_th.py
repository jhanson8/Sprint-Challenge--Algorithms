'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    target = "th"
    target_len = len(target)

    #Base Case 
    if len(word) == 0 or len(word) < target_len:
        return 0 
    
    #check if word matches target exactly
    if word[0:target_len] == target:
        return count_th(word[target_len-1:]) + 1
    
    #else check for "th" through remaining indexes
    else:
        return count_th(word[target_len-1:])
    

    
