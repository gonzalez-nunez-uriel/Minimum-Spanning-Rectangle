import numpy as np
from Vector import Vector

#x and y must be np arrays
#changes from an old base at 0,0 into a new base
#the new base needs to be given in terms of the old base
#pp_org >> original parametrization point. Must be of type Vector
#tuv >> tangential unit vector
#nuv >> normal unit vector
def changeOfBases( x, y, pp_org, tuv, nuv ):

    print('starting change of bases')
    #x and y should have the same size
    N = x.size

    t = np.empty( ( N, 1 ), dtype = float )
    n = np.empty( ( N, 1 ), dtype = float )

    #for every point (x,y)
    for i in range( 0, N ):

        #all this operations could be done without the vector data structure
        #but this is more convenient
        currentVector = Vector( x[i], y[i] )

        #at this point, the new vector is still defined with the original bases
        #but its components are with respect to the new parametrization point
        newVector = currentVector - pp_org

        #find each individual projection and store
        t[i][0] = newVector * tuv
        n[i][0] = newVector * nuv

    #this returns the new coorditantes of the same point under the new bases
    return ( t, n )
