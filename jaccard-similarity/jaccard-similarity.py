def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set_a , set_b = set(set_a) , set(set_b)
    if set_a == None and set_b == None:
        return 0,0
    else:
        if len(set_a | set_b) == 0:
            return 0
        else:
            j = len(set_a & set_b)/ len(set_a | set_b) 
            return j 
    