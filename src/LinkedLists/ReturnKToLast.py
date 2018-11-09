#return the Kth element in a singly linked list
#again i wont use fancy python stuff and pretend it's a normal list

def getKToLast(slist, k):
    count = 0
    ihead = iter(slist)
    itailing = iter(slist)
    kvalue = None
    for elem in slist:
        if count >= k:
            kvalue = next(itailing)
        count += 1
    return kvalue