#Remove duplicates from an unsorted list
#I will iterate through this like a normal list instead of using fancy python stuff

def removeDups(unsortList):
    d = dict()

    i = iter(unsortList)
    for elem in i:
        if elem in d:
            unsortList.remove(elem)
        d[elem] = True

    return unsortList

def removeDupsNoBuffer(unsortList):

    i1 = iter(unsortList)
    for elem1 in i1:
        i2 = i1.copy()
        for elem2 in i2:
            if elem1 == elem2:
                unsortList.remove(elem2)
                break

    return unsortList
