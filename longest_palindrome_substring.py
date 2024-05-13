def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    answer = ""
    resLen = 0

    for i in range(len(s)):
        # For answers that are odd
        left, right  = i ,i
        while left >=0 and right < len(s) and s[left] == s[right]:
            if(right - left + 1) > resLen:
                answer = s[left : right + 1]
                resLen = right - left + 1
            right += 1
            left -= 1

        # For answers that are even 
        left, right  = i , i+1
        while left>=0 and right <len(s) and s[left] == s[right]:
            if (right - left + 1) > resLen:
                answer = s[left : right+1 ]
                resLen = right - left + 1
            right += 1
            left -= 1
    return answer

print(longestPalindrome("abbabaabababa"))
