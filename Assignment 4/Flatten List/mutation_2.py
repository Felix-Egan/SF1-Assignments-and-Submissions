def flatten_list(lst):
    '''
    Changed the append method to extend method in the else block. 
    '''
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.extend(i)
    return result