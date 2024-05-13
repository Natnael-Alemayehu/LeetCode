def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) <=1:
        return len(s)
    
    left = answer = 0
    dictionary = {}

    for right, letter in enumerate(s):
        if letter in dictionary:
            if dictionary[letter] >= left:
                left = dictionary[letter] + 1
        answer = max(answer , right - left + 1)
        dictionary[letter] = right
    return answer

print(lengthOfLongestSubstring("aab"))