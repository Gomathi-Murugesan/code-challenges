def fun_alpha(s):
    output=False
    for i in s:
        if i.isalpha():
            output=True
    return output

def fun_alphanum(s):
    output=False
    for i in s:
        if i.isalnum():
            output=True
    return output

def fun_num(s):
    output=False
    for i in s:
        if i.isdigit():
            output=True
    return output

def fun_lower(s):
    output=False
    for i in s:
        if i.islower():
            output=True
    return output    

def fun_upper(s):
    output=False
    for i in s:
        if i.isupper():
            output=True
    return output

if __name__ == '__main__':
    s = input()
    print(fun_alphanum(s))
    print(fun_alpha(s))
    print(fun_num(s))
    print(fun_lower(s))
    print(fun_upper(s))
