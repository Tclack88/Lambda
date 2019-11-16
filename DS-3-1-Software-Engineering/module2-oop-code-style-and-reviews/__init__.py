"""
lambdata - test for creating helper functions
"""

def flatten(lst):
    """ 
    flattens lists, any combination of lists within lists
    will be converted into one long list 
    """
    return sum( ([x] if not isinstance(x, list) else flatten(x) for x in lst), [] )

