
#should I import anything?

#parametrization center
#magnituded of parametrization vector
#parametrization point
#displacement along parametrization line
def findRotatedParametrizationVectors(pc,mpr,pp,dapl):

    #parametrization displacement point
    pdp = pp + dapl
    print('parametrization displacement point: ' + str(pdp))

    #parametrization direction vector
    pdv = pdp - pc
    print('parametrization direction vector: ' + str(pdv))

    #parametrization direction unit vector
    pduv = pdv.unitVector()
    print('parametrization direction unit vector: ' + str(pduv))

    #parametrization radius vector
    prv = pduv ** mpr
    print('parametrization radius vector: ' + str(prv))

    #new parametrization point
    npp = pc + prv
    print('parametrization point: ' + str(npp))

    return ( prv, npp )
