def isValid(s):
    val = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    open_char = ["[", "(", "{"]
    close_char = ["]", "}", ")"]
    stack = []
    ans = True
    for i in s:
        if i in open_char:
            stack.append(i)
        elif i in close_char:
            if len(stack) != 0:
                popped = stack.pop()
                if val[i] == popped:
                    ans = True
                else:
                    ans = False
                    return ans
            else:
                return False
    if len(stack) != 0:
        return False
    return ans


print(isValid("({[{}]})"))
