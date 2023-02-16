import random
import string

with open("contest_2_test_2.txt","w+") as ifile:
    letters = string.ascii_lowercase
    line = ''.join([random.choice(letters) for i in range(100000)])
    ifile.write(line)