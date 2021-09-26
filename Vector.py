from math import sqrt
from math import cos
from math import sin

def testLib():
    print('lib working')


def magnitudeAndSlopeToVector( magnitude, slope ):

    #does not preserve the sign
    t = sqrt( ( magnitude ** 2 ) / ( slope ** 2 + 1 ) )
    #preserves the sign
    n = slope * t

    return Vector( t, n )

#data structure to handle vectors
class Vector:

    def __init__( self, v_1, v_2 ):
        self.t = v_1
        self.n = v_2


    def __add__( self, v_2 ):

        t = self.t + v_2.t
        n = self.n + v_2.n

        return Vector( t, n )


    def __sub__( self, v_2 ):

        t = self.t - v_2.t
        n = self.n - v_2.n

        return Vector( t, n )


    def __mul__( self, v_2 ):

        return self.t * v_2.t + self.n * v_2.n

    #BUG--> order matters, scalar must be the second one
    def __pow__( self, someScalar ):
        t = self.t * someScalar
        n = self.n * someScalar

        return Vector( t, n )


    def __str__( self ):

        return '<' + str(self.t) + ',' + str(self.n) + '>'


    def magnitude( self ):

        return sqrt( self.t**2 + self.n**2 )


    def scalarToVector( self, scalar ):

        return Vector( scalar, scalar )


    def unitVector( self ):

        m = self.magnitude()

        t = self.t / m
        n = self.n / m

        return Vector( t, n)

    #these two are inefficient. A better approach is needed
    def tangentalUnitVector( self ):

        return Vector( self.unitVector().t, 0 )


    def normalUnitVector( self ):

        return Vector( 0, self.unitVector().n )
