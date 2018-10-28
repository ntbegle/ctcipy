
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