# import sys and getopt in order to read console arguments
import sys
import getopt
# import structure used to view data
from lab_work.structure import Detail
# import random for genration of pivot element 
import random

# Evaluation and check of console argument
def evaluateCmdArgs(argv):
    # default input and output files in case not provided in console
    inputFile = "data.txt"
    outputFile = "result.txt"
    # extarcts string from console and parses it into arguments and corresponding values
    opts, args = getopt.getopt(argv,"s:f:o:",["ifile=","ofile="])
    for opt, arg in opts:
        # sort method
        if opt == '-s':
            if arg.lower() in ["quicksort","binarysort","sort"]:
                sortType = arg.lower()
            else:
                sys.exit()
        # field parameter by which sorting is performed
        elif opt == "-f":
            if arg.lower() in ["name","id","amount"]:
                sortParameter = arg.lower()
            else:
                sys.exit()
        # order of sorting
        elif opt == "-o":
            if arg.lower() in ["asc","desc"]:
                sortDirection = True if arg.lower()=="desc" else False
            else:
                sys.exit()
        # optional input and output threads
        elif opt == "--ifile":
            inputFile = arg
        elif opt == "--ofile":
            outputFile = arg
    return inputFile,outputFile,sortType,sortParameter,sortDirection

# performs quick sort and returns result based on direction of sorting
def quickSort(data: list, parameter: str, direction: int):
    # define quicksort
    def quicksort(array: list, key: str):
        if len(array) <= 1:
            return array
        else:
            pivot_el = random.choice(array)
            l_nums = [el for el in array if el.getFieldValue(key) < pivot_el.getFieldValue(key)]
            e_nums = [pivot_el] * array.count(pivot_el)
            b_nums = [el for el in array if el.getFieldValue(key) > pivot_el.getFieldValue(key)]
            return quicksort(l_nums, parameter) + e_nums + quicksort(b_nums, parameter)

    # perform quick sort
    data = quicksort(data,parameter)

    # reverse array in case direction is ascending
    if direction==False:
        return data[::-1]

    return data

# performs binary intersection sort and returns result based on direction of sorting
def binarySort(data: list, parameter: str, direction: int):

    # define binary sort
    def InsertionSort_improved(array: list):
        for k in range(1,len(array)):
            key = array[k]
            low = 0
            high = k-1
            BinarySearch(array,low,high,key,k)

    def BinarySearch(array: list, low: int, high: int, key: Detail, k: int):
        if low<high:
            mid= (low+high)//2
            if array[mid].getFieldValue(parameter) == key.getFieldValue(parameter):
                for i in range(k,mid,-1):
                    array[i] = array[i-1]
                array[i-1] = key
            elif array[mid].getFieldValue(parameter) < key.getFieldValue(parameter):
                BinarySearch(array, mid+1, high, key, k)
            else:
                BinarySearch(array, low, mid, key, k)
        else:
            mid=(low+high)//2
            if array[mid].getFieldValue(parameter)>key.getFieldValue(parameter):
                for j in range(k,mid,-1):
                    array[j] = array[j-1]
                array[j-1] = key

    # perform binary sort
    InsertionSort_improved(data)

    # reverse array in case direction is ascending
    if direction==False:
            return data[::-1]

    return data

# reads Data from input thread (external file) and returns list of detail objects
def readData(fileName:str):
    try:
        # open input thread and read data from file
        dataFile = open(fileName,"r")
        dataStorage = dataFile.readlines()
        # empty list to store Details
        details_list = []
        # parse result lines into list of Detail objects
        for obj_data in dataStorage:
            obj_data=obj_data.split(";")
            detail = Detail(id=obj_data[0],name=obj_data[1],amount=obj_data[2])
            details_list.append(detail)
        # close thread
        dataFile.close()
        return details_list
    except Exception as e:
        print(e)
    return None

# writes list of detail objects into output thread (external file)
def writeData(fileName: str, data: list):
    try:
        # open output thread on writing
        dataOutputFile = open(fileName,"w")
        # write lines into output file via overrode __str__
        for obj_data in data:
            dataOutputFile.write(obj_data.__str__())
        # close thread 
        dataOutputFile.close()
    except Exception as e:
        print(e)

# fork-method defines type of sorting to perform based on data from console arguments 
def performSorting(data: list, sortType:str, sortParameter: str, sortDirection: bool):
    if sortType == "quicksort":
        return quickSort(data=data, parameter = sortParameter, direction = sortDirection)
    elif sortType == "binarysort":
        return binarySort(data=data, parameter = sortParameter, direction = sortDirection)
    elif sortType == "sort":
        return sorted(data,key=lambda detail:detail.getFieldValue(sortParameter), reverse=sortDirection)