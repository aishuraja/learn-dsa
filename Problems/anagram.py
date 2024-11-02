str1 = "dog"
str2 = "god"

# python function

def check_ana(s1, s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) != sorted(s2):
        return False
    return True

print(check_ana(str1, str2))