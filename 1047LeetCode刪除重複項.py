def removeDuplicates(S: str) -> str:
    stk = list()
    for ch in S:
        if stk != [] and stk[-1] == ch:
            stk.pop()
        else:
            stk.append(ch)
    return "".join(stk)

S = 'abbaca'
ans = removeDuplicates(S = S)
print('ans: ' + ans)










