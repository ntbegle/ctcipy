#Replace all spaces in string with %20

#since python passes by value we can't change what was passed in so we have to return it
#will pass in a list of characters instead of a string since strings are immutable in python

# loop through string backwards.  when a space is reached, start from the end of string and move it down by 2.  replace
#   current position with %20 and decrement idx by 2 to the next char. increment length by 2.
#   time complexity of this is nlogn
#
# this can be done in O(n) time by making a copy of the string

def replaceSpaces(url, urlLen):
    for i in range(urlLen-1, -1, -1):
        if url[i] == ' ':
            for j in range(urlLen-1, i, -1):
                url[j+2] = url[j]
            url[i] = '%'
            url[i+1] = '2'
            url[i+2] = '0'
            urlLen += 2
    return url
