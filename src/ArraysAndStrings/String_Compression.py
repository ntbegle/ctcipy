#compress string by replacing the repeated characters with the char and it's number of repetitions

def compressStr(uncompStr):
    compStrArr = []
    curLetter = ''
    curLetterCnt = 0

    for c in uncompStr:
        if curLetter == c:
            curLetterCnt += 1
        else:
            if curLetter != '':
                compStrArr.append(curLetter + str(curLetterCnt))
            curLetter = c
            curLetterCnt = 1
    if curLetter != '':
        compStrArr.append(curLetter + str(curLetterCnt))

    compStr = str('').join(compStrArr)

    if len(compStr) >= len(uncompStr):
        return uncompStr
    else:
        return compStr