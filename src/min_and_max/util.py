import numpy as np
import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')

def min_max():

    N, _ = input().split()
    N = int(N)

    arr = [list(map(int, input().split())) for _ in range(N)]

    min_col=np.min(arr,axis =1)
    result=np.max(min_col,axis=0)
    logging.info(result)
    return result
