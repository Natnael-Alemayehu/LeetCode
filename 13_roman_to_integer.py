def romanToInt(s):
    reference = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    answer = 0

    for i in range(len(s)):
        if i + 1 < len(s) and reference[s[i]] < reference[s[i + 1]]:
            answer -= reference[s[i]]
        else:
            answer += reference[s[i]]

    return answer


print(romanToInt("MCMXCIV"))
