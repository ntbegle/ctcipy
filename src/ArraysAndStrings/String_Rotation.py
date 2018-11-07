#Given 2 strings, write code to check if string 2 is a rotation of string 1 using only 1 call
#to check if it is a substring

def isRotation(s1, s2):
    doubleStr = s1 + s1
    if s2 not in doubleStr:
        return False
    else:
        return True