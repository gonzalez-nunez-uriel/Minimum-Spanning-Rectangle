#should I import Vector?
#should I import numpy?

def findReferenceSlope( pr ):
    #choose a random angle in the furthest circle that is valid
    #to know if its valid, first determine the quadrant relative to the mean
    #then using the distance vector betweent the mean and center, choose a random ...
    #it doesnt need to be random ...
    #use the same angle as that of the distanace vector
    #this way, you ensure that no invalid line is made upoin initialization
    #its not a bad idea to initialize to a rectangle that is clearly bigger than it should be


    #a special case that needs to be handled
    #THIS CASE IS A HEADACHE!!!
    if pr.t != 0:

        slope = pr.n / pr.t

        #we wish to find the line perpendicular to {}
        #for a line with slope m the slope of the perpendicular is -1/m
        #sing_dv_x * sing_dv_y >> true sign of the slope
        reference_slope = -1 / slope
    else:
        #special case
        reference_slope = 0
        #THE OTHER SPECIAL CASE WHEN THE SLOPE = 0 IS NOT COVERED


    return reference_slope
