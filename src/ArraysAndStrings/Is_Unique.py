
#implement an algorithm to determine if string has all unique characters
#input is a string
#output is true if string is unique, false otherwise
def is_unique(s):
    charDict = dict()
    for c in s:
        if c in charDict:
            return False
        else:
            charDict[c] = True
    return True

def is_unique_no_ds(s):
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return False


    return True




