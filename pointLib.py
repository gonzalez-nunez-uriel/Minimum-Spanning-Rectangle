#library for finding points with desired properties
#its supposed to handle np arrays, should I import numpy?

#this function computed the leftmost value of each circle
def leftmost( tangential_values, radius ):

    leftmost_values = tangential_values - radius

    return leftmost_values

def meanPoint( x, y ):

    n = x.size

    return ( x.sum()/n, y.sum()/n )

#this function computed the bottommost value of each circle
def nadir( normal_values, radius ):
    nadir_values = normal_values - radius
    return nadir_values

#this function computed the rightmost value of each circle
def rightmost( tangential_values, radius ):

    rightmost_values = tangential_values + radius

    return rightmost_values

#this function computed the topmost value of each circle
def zenith( normal_values, radius ):
    zenith_values = normal_values + radius
    return zenith_values
