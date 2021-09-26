#--comment here --

import numpy as np
import mainLib
import pointLib
from findReferenceSlope import findReferenceSlope
from Vector import Vector
from Vector import magnitudeAndSlopeToVector
from math import tan

EPOCHS = 2
LR = 0.524078

print('START OF PROGRAM')

inputFile = open('rectangles.txt', 'r')

( x, y, r ) = mainLib.parseInputFileToMatrix( inputFile )

#no need for the input file any more
inputFile.close()

( x_avg, y_avg ) = pointLib.meanPoint( x, y )

meanVector = Vector( x_avg, y_avg )

#we know which circle and how far it is from the mean >> but we only care about the general direction
i_fur, pc, pr, pp  = mainLib.findParametrizationVectors( meanVector, x, y, r )

'''
#parametrization point
#this point is described in the original (x,y) coordinates
pp = dftm + meanVector

#parametrization center as a vector in terms of (x,y) coordinates
pc = Vector( x[i_fur], y[i_fur] )

#parametrization radius
#described with respect to the center of the circle with the furthest point
pr = dftm - ( pc - meanVector )
'''

#at this point, we have the base case for our algorithm

#flag to control execution
keepGoing = True

#magnitude of parametrization radius
mpr = r[i_fur]

#An initial value
minArea = mainLib.areaOfSpanningRectangle( x, y, r, meanVector, pr, pp )
print('original area:' + str( minArea ) )
print('\n\n\n')
#HERE IS WHERE THE LOOP TAKES PLACE
print('----------')
print('starting greedy algorithm\n')
print('parametrization center: ' + str(pc))
print('parametrization point: ' + str(pp))
print('parametrization radius: ' + str(pr))
print('comp: ' + str(pc+pr))
print('----------')

while( keepGoing ):

    #these are needed for set up
    reference_slope = findReferenceSlope( pr )

    #tuv >> tangent unit vector along the reference line
    tuv = magnitudeAndSlopeToVector( 1, reference_slope )

    #nuv >> normal unit vector
    #perpendicular to tuv and also points towards the inside of the points
    #towards the inside is the opposite of pr
    nuv = Vector( -1 * pr.t, -1 * pr.n ).unitVector()
    print('unit vevtors:')
    print('tuv: ' + str(tuv) + 'nuv: ' + str(nuv))

    print('\nPOSITIVE DISPLACEMENT')

    #positive Displacement Along The Paprametrization Line
    pdapl = tuv ** LR
    print('Positive Displacement Along The Paprametrization Line: ' + str(pdapl))

    #positive displacement parametrization vector
    #positive displacement parametrization point
    pdprv, pdpp = mainLib.findRotatedParametrizationVectors(pc,mpr,pp,pdapl)

    positiveDisplacementArea = mainLib.areaOfSpanningRectangle( x, y, r, meanVector, pdprv, pdpp )
    print('pd area: ' + str(positiveDisplacementArea))

    print('\nNEGATIVE DISPLACEMENT')
    #negative Displacement Along The Paprametrization Line
    ndapl = tuv ** ( -1 * LR )
    print('Negatvie Displacement Along The Paprametrization Line: ' + str(ndapl))

    #negative displacement parametrization vector
    #negative displacement parametrization point
    ndprv, ndpp = mainLib.findRotatedParametrizationVectors(pc,mpr,pp,ndapl)

    negativeDisplacementArea = mainLib.areaOfSpanningRectangle( x, y, r, meanVector, ndprv, ndpp )
    print('nd area: ' + str(negativeDisplacementArea))

    

    keepGoing = False
    ##############






print('\nEND OF PROGRAM')
