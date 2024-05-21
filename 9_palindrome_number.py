def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x<0:
        return False
    return (True if x-int((str(x))[::-1]) == 0 else False)
    
print(isPalindrome(1221))