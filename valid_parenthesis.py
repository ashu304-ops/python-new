#close>open return false
#length iis odd return false
#id type is not matched return false
#stack empty it is true and valid
#pair willl be eliminated from stack

def isvalid(s:str) -> bool:
    stack=[]
    pair={'(':')','[':']','{':'}'}
    for char in s:
        if char in pair:
            stack.append(char)
        elif char in pair.values():
            if not stack or pair[stack.pop()]!=char:#
                return False
    return not stack

input_string=input('enter the parentensis')

if isvalid(input_string):
    print('thr string is valid')
else:
    print('string is invalid')


    