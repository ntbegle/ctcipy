# given 2 strings, is the first string one edit away from being the same as the second string
# An edit is defined as an add, remove, and replace

def isOneAwayToEq(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    errCnt = 0
    idx1 = 0
    idx2 = 0
    while idx1 < len(str1) and idx2 < len(str2):
        if str1[idx1] != str2[idx2]:
            errCnt += 1
            if len(str1) > len(str2):
                idx1 += 1
            elif len(str1) < len(str2):
                idx2 += 1
            else:
                idx1 += 1
                idx2 += 1
        else:
            idx1 += 1
            idx2 += 1


    return errCnt < 2