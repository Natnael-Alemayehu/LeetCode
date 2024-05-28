def longestCommonPrefix(strs):
    answer = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return answer
        answer += strs[0][i]


print(longestCommonPrefix(["flower", "flow", "flght"]))
