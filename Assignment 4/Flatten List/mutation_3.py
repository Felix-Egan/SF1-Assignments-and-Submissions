def flatten_list(lst):
    '''
    
    '''
    result = []
    for i in lst:
        if type(i) == list:
            result += (flatten_list(i))
        else:
            result.append(i)
    return result