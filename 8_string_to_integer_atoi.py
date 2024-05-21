def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    
    s = s.lstrip()
    if s =="":
        return 0
    
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    if s[0] in numbers:
        read_sign = True
    elif s[0] == "-":
        read_sign = False
        s = s[1:]
    elif s[0] == "+":
        read_sign= True
        s=s[1:]
    else:
        read_sign = True
        
    
    num_str = ""
    for number in s:
        if number in numbers:
            num_str += number
        else:
            break
    if num_str == "": num_str = "0"
    if read_sign:
        num_str = int(num_str)
        if num_str < 2**31 -1:
            return num_str
        else: 
            return 2**31-1
    else:
        num_str = int("-"+num_str) 
        if num_str > -2**31:
            return num_str
        else:
            return -2**31
    
    
print(myAtoi("+1"))