
#inputArray needs to be a numpy array...or maybe not?
#if not, that is a good programming practice
#in the programm I use it will be. Should I import numpy?
#inputIndexes >> a python array(not numpy) that contains a list of the indexes
#passed to the function. This is done so that if you found indexes with some
#property A, you can then find the max of the indexes with that property.
def findMaxIndexesInArray( inputArray, inputIndexes = None ):

    #for intensive computations, np arrays are preferrable
    #but if the task is with selection and comparisons of just some values
    #regular arrays are more efficient --> np arrays are overkill
    indexes = []

    #a number sufficiently negative
    maxValue = -100000

    #i is the indexes in the inputArray, but they might be defined relative to
    #the indexes in inputIndexes. That is handled latter
    for i in range( 0, inputArray.size ):

        currentValue = inputArray[i]

        if currentValue >= maxValue:

            #every time there is a number strictly greater than maxValue, you need to flush the index array
            if currentValue > maxValue:
                indexes = []

            maxValue = currentValue
            indexes.append(i)

    #this is a conditional allows the caller to give the indexes that are being checked
    #this way you can do some other filter before calling this function
    #or calling this function several times
    #it extends functionality by making it more general
    if inputIndexes != None:
        result = []
        #indexes contains the count relative to inputArray
        for j in indexes:
            #extracts the jth index, which is the correct index
            result.append( inputIndexes[j] )
            #returns results and terminates execution
            return result

    return indexes
