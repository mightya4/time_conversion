#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time_constraint = ''.join([i for i in s if i.isalpha()])
    curr_time = ''.join([i for i in s if not i.isalpha()])
    if time_constraint == "PM":
        #add 12 plus current time
        if curr_time[0] != "1" and curr_time[1] != "2":
            tmp_time = list(curr_time)
            tmp_time[0] = str(1 + int(tmp_time[0]))
            tmp_time[1] = str(2 + int(tmp_time[1]))
            curr_time = "".join(tmp_time)
    else:
        #check if time is 12 am
        if curr_time[0] == "1" and curr_time[1] == "2":
            tmp_time = list(curr_time)
            tmp_time[0] = "0"
            tmp_time[1] = "0"
            curr_time = "".join(tmp_time)
        else:
            pass
    
        
    print(f"{curr_time}")
    return curr_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
