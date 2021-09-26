import numpy as np

#this function reads from file and properly formats the data
def parseInputFileToMatrix( file ):

    #it is easier to just use python arrays and then convert them to numpy arrays latter
    #this is to prevent issues of memory preallocation
    x = []
    y = []
    r = []

    currentLine = file.readline()

    while currentLine != '' and currentLine != '\n':

        x_str_from_file, y_str_from_file, r_str_from_file  = currentLine.split( ' ' )

        x.append( float( x_str_from_file ) )
        y.append( float( y_str_from_file ) )
        r.append( float( r_str_from_file ) )

        currentLine = file.readline()

    #memory allocation for numpy arrays using the size of the python array
    #would this really be more efficient? What is the cost of the append function?
    #In another file, I counted the number of lines and did the preallocation beforehand
    #I think that is more efficient
    #but the number of reads from file in the other approach is twice the one here
    #but this one has append
    #which is more efficient?
    #It clearly is not memory efficient
    x_np = np.empty( ( len( x ), 1 ), dtype = float )
    y_np = np.empty( ( len( y ), 1 ), dtype = float )
    r_np = np.empty( ( len( r ), 1 ), dtype = float )

    for i in range( 0, len( x ) ):
        x_np[i] = x[i]
        y_np[i] = y[i]
        r_np[i] = r[i]

    #allows other callers to use the file
    file.seek(0)

    return ( x_np, y_np, r_np )
