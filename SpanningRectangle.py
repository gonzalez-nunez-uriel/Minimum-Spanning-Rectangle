

def compareSpaningRectangles(current, positiveDisplacement, negativeDisplacement):

    if positiveDisplacement.area < negativeDisplacement.area:
        if positiveDisplacement.area < current.area
            return positiveDisplacement
        else:
            return current
    else:
        if negativeDisplacement.area < current.area
            return negativeDisplacement
        else:
            return current

class SpanningRectangle:

    def __init__(pc, pr, pp, area = None):
        self.pc = pc
        self.pr = pr
        self.pp = pp
        self.area = area
