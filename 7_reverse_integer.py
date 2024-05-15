def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x<0:
        if x > -2**31:
            x = str(x)
            x = x[1:]
            x = x[::-1]
            x = -int(x)
            if x > -2**31:
                return x
            else: return 0
        
        else: return 0
    else:
        if x < 2**31 -1:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x < 2**31 -1:
                return x
            else: return 0
        else: return 0
