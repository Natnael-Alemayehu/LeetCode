def zigzag_conversion(s, numRows):
    if numRows == 1: return s
    
    answer = ""
    for row in range(len(s)):
        inc = 2 * (numRows - 1)
        for i in range(row , len(s), inc):
            answer += s[i]
            if (row>0 and row<numRows-1 and (i+inc-2*row)<len(s)):
                answer += s[i+inc-2*row]
    return answer
print(zigzag_conversion("PAYPALISHIRING",3))