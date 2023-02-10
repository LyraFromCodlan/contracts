# main file/ starting point of the programm 

# all the essential libraries used in lab5 are already included here
from external_functions import *

def main(argv):
    # try component in order to handle errors on the runtime
    try:
        # evalutaion of the console arguments and their extraction into parameters
        inputFile,outputFile,sortType,sortParameter,sortDirection = evaluateCmdArgs(argv=argv)
        # extract list of details from source file 
        data = readData(fileName=inputFile)
        # depending on console arguments perform sorting and return sorted list of details
        data = performSorting(data=data,sortType=sortType,sortParameter=sortParameter,sortDirection=sortDirection)
        # writing sorted details list in output thread(file)
        writeData(fileName=outputFile, data=data)
    except Exception as e:
        print(e)

if __name__=="__main__":
    main(sys.argv[1:])