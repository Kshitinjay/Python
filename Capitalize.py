#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    word = s.split(" ")
    x = (i.capitalize() for i in word)
    return ' '.join(x)    



if __name__ == '__main__':