#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def time_delta(t1, t2):
    t1_date = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2_date = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    if t1_date > t2_date:
        time_diff = t1_date - t2_date
    else:
        time_diff = t2_date - t1_date
    if time_diff.days == 0:
        time_diff_seconds = time_diff.seconds
    else:
        time_diff_seconds = time_diff.days * 24 *3600 + time_diff.seconds
    return str(time_diff_seconds)

def time_diff():

    t = int(input())
    result=""

    for _ in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        logging.info(delta)
        result+=delta+'\n'
    return (result)