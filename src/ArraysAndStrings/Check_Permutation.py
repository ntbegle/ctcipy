
#possible solutions
#   1. brute force by looping over chars in str1 and seeing if it exists in str2
#       need to make sure duplicates are captured.  this can be done by creating a marker array
#       to mark when a letter has been used
#   2. sort strings and them loop through both at the same time and check that the chars match
#       this won't take into account equal strings (is that a permutation???)
#       this will have O(nlogn) time complexity
#   3. create dictionaries of chars in the strings, one dict for each string.  make sure count of
#       chars in dictionaries match.
#       3 total loops giving time complexity of O(n)
#   4. another way I read about online is to only use one dict.  Increment value by 1 if it exists in str1
#       decrement if it exists in str2.  final values in dict should all be 0

# use option 4
def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    charDict = dict()

    for i in range(0,len(str1)):
        if str1[i] in charDict:
            charDict[str1[i]] += 1
        else:
            charDict[str1[i]] = 1

        if str2[i] in charDict:
            charDict[str2[i]] -= 1
        else:
            charDict[str2[i]] = -1

    for v in charDict.values():
        if v != 0:
            return False

    return True


# def isPalindrome(inputStr):
#     startIdx = 0
#     endIdx = len(inputStr) - 1
#
#     while startIdx < endIdx:
#         if inputStr[startIdx] != inputStr[endIdx]:
#             return False
#     return True

# check input string if a permutation exists that is a palindrome
# example in book ignores spaces so i guess i will too
#   if it's a palindrome then the count of individual chars should be even unless it has an odd amount of chars
#       which means only 1 char can have on odd count
def isPalindromePermutation(inputStr):
    charDict = dict()
    strLen = len(inputStr)
    # fill charDict with char counts for each char
    for c in inputStr:
        if c != ' ':
            if c in charDict:
                charDict[c] += 1
            else:
                charDict[c] = 1
        else:
            strLen -= 1

    numOdd = 0
    for v in charDict.values():
        if (v % 2) == 1:
            numOdd += 1

    if (strLen % 2) == 0 and numOdd > 0:
        return False
    elif (strLen % 2) == 1 and numOdd > 1:
        return False
    return True