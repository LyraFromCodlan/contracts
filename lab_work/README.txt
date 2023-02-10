Purpose of the utility program:
Sort data about details

Python veersion: 3.10

Used libraries: random, sys, getopt

Instructions:

1) Clone repository to the local directory via cmd console:
    git clone https://github.com/LyraFromCodlan/contracts.git

2) Check if file "data.txt" with abstract data is present or upload your own

    Data file must have '.txt' extension and follow next structue:
        - each line contains info about detail in following order: ID; name; amount of items;
        - each line must contain all 3 values and them alone
        - values in the row must be separated by ";"
        - number of rows in file must match the number of details

        Example:
        UID21;Detail_name;21;

3) To run the program use command promt:

    console command have following structur:
    
        python lab5.py -s *sort method* -f *parameter to sort by* -o *sort order* --ifile *input file name with '.txt' extension* --ofile *output file name with '.txt' extension*

    - sorting methods available to use have next names:
        1 - quicksort - uses quick sort;
        2 - binarysort - uses insertion sort with binary search;
        3 - sort - uses Pythons standard library method sorted();

    - sorting parameter available to use have next names:
        1 - id;
        2 - name;
        3 - amount;

    - sorting order available to use have next names:
        1 - asc - ascending order
        2 - desc - descenging order

    - optional file parameters must have file name with '.txt' extension. If not mentioned standard name "data.txt","result.txt" used.

    Example:
        python lab5.py -s sort -f name -o desc --ifile data.txt --ofile sorted_data.txt
    or
        python lab5.py -s quicksort -f id -o asc