
from collections import namedtuple

import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')

def avg_marks():

    n = int(input())

    s_data = namedtuple('Students', input())
    class_marks = [int(s_data(*input().split()).MARKS) for _ in range(n)]
    logging.info(sum(class_marks) / len(class_marks))
    return sum(class_marks) / len(class_marks)