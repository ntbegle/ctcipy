
#implement an algorithm to determine if string has all unique characters
#input is a string
#output is true if string is unique, false otherwise
def is_unique(str):
    charDict = dict()
    for c in str:
        if c in charDict:
            return False
        else:
            charDict[c] = True
    return True

def is_unique_no_ds(str):
    for i in range(0,len(str)-1):
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                return False


    return True

testStrs = ['abcde', 'hello world', 'aabcd', 'abcdd']

for str in testStrs:
    if is_unique(str):
        print('Test str \''+ str + '\' is unique')
    else:
        print('Test str \'' + str + '\' is not unique')

for str in testStrs:
    if is_unique_no_ds(str):
        print('Test with no data structs str \''+ str + '\' is unique')
    else:
        print('Test with no data structs str \'' + str + '\' is not unique')

