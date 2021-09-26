import pointLib
from findReferenceSlope import findReferenceSlope
from Vector import Vector
from Vector import magnitudeAndSlopeToVector
from changeOfBases import changeOfBases

#this one is going to be tricky

def areaOfSpanningRectangle( x, y, r, meanVector, pr, pp ):

    reference_slope = findReferenceSlope( pr )

    #tuv >> tangent unit vector along the reference line
    tuv = magnitudeAndSlopeToVector( 1, reference_slope )

    #nuv >> normal unit vector
    #perpendicular to tuv and also points towards the inside of the points
    #towards the inside is the opposite of pr
    nuv = Vector( -1 * pr.t, -1 * pr.n ).unitVector()
    print('unit vevtors:')
    print('tuv: ' + str(tuv) + 'nuv: ' + str(nuv))

    #the function requires all the points, the new origin, and each of the axes
    #t >> all points tranformed with respect to tuv
    #n >> all points transformed with respect to nuv
    t, n = changeOfBases( x, y, pp, tuv, nuv )

    print('Flächenberechnung')

    ze = pointLib.zenith( n, r )
    na = pointLib.nadir( n, r )
    lf = pointLib.leftmost( t, r )
    rg = pointLib.rightmost( t, r )

    height = max( ze ) - min( na )
    base = max( rg ) - min( lf )
    print('height: ' + str(height) + ' base: ' + str(base))

    return height * base
