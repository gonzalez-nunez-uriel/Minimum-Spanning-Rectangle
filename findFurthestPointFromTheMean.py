import numpy as np
from findMaxIndexesInArray import findMaxIndexesInArray
from Vector import Vector
from Vector import magnitudeAndSlopeToVector
from math import atan

#x and y must be np arrays
#x and y are cartegian coordinates
#r is the radius of each (x,y)
#returnIndexes allows the caller to see at which indexes the max occurs
def findFurthestPointFromTheMean( meanVector, x, y, r ):

    print('finding furthest point fromt the mean')

    #to find the furthest point from the mean we need to account for the radius
    #of the circles. To achieve this, it is necessary to use Vectors to find the
    #direction of the distance from the mean. After that we can find the findMaxIndexesInArray

    #for every pair there is another pair
    n = x.size
    #x_r >> x plus radius
    #y_r >> y plus radius
    x_r = np.empty( ( n, 1 ), dtype = float)
    y_r = np.empty( ( n, 1 ), dtype = float)


    for i in range( 0, n ):

        currentVector = Vector( x[i], y[i] )

        #mean to center vector
        #a vector that points from the mean to the center of the circle
        mtcv = currentVector - meanVector
        mtcuv = mtcv.unitVector()

        #the tangent is the x coordinate
        #the normal is the y coordinate
        #scalar streching of the unit vector
        radiusVector = mtcuv ** r[i]
        #radiusVector = Vector( r[i] * mtcuv.t, r[i] * mtcuv.n )

        #vector that points from the mean to the point in the circle furthest from the mean
        distanceVector = mtcv + radiusVector

        #storing components
        x_r[i] = distanceVector.t
        y_r[i] = distanceVector.n

    #at this point, all the furthest points from the mean for each circle are in
    #x_r and y_r

    #compute L1 norm
    distance_L1norm = np.abs( x_r ) + np.abs( y_r )

    indexes = findMaxIndexesInArray( distance_L1norm )

    #if there are more than one indexes givin a max
    if len(indexes) > 1:
        #the number of distances that are equal should be small
        #its ok to use regular arrays
        distance_L2norm = []

        #computing L2 norm
        for i in indexes:
            #sqrt is an order preserving function
            #therefore, we do not need to compute it if we want to find the max
            currentDistance = x_r[i]**2 + y_r[i]**2
            distance_L2norm.append( currentDistance )

        #it is necessary to give the current list of indexes
        indexes = findMaxIndexesInArray( distance_L2norm, indexes )

    #assuming that there is more than one index - which is unlikely - then we need to choose randomly one
    #but the input itself is somewhat random, right
    #since indexes is still an array, just select element zero and be done
    #IF the input file is not random, then THIS NEEDS TO BE CHANGED
    i = indexes[0]

    #distance from the mean
    dftm = Vector( x_r[i], y_r[i] )

    return ( i, dftm )
