import sys

line = sys.stdin.readline()

def strvaild(string): # "(cool)"
    
    bracket_map = {"(":")", "[":"]", "{":"}"}
    open_bracket = set(["(", "[", "{"])
    stack = []
    
    for word in string:
        if word in open_bracket:
            stack.append(word)
            
        elif stack and word == bracket_map[stack[-1]]:
            stack.pop()           
            return True

        else:
            return False
strvaild(line)
# str1 = "()"
# str2 = "[]"
# str3 = "{}"
# str4 = "[}"
# str5 = "{)"
# str6 = "([{}])"
# str7 = "{[]}"
# print(strvaild(str1))
# print(strvaild(str2))
# print(strvaild(str3))
# print(strvaild(str4))
# print(strvaild(str5))
# print(strvaild(str6))
# print(strvaild(str7))
