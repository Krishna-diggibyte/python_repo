import numpy as np
import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')

def mean_var():
    n, m = map(int, input().split())

    arrays = np.array([input().split(" ") for _ in range(n)], int)

    # Print stats
    result=""
    # logging.info(np.mean(arrays, axis=1))
    # logging.info(np.var(arrays, axis=0))
    # logging.info(round(np.std(arrays, axis=None), 11))
    a=np.mean(arrays, axis=1)
    result+= str(a)+'\n'
    result+=str(np.var(arrays, axis=0))+'\n'
    result+=str(round(np.std(arrays, axis=None), 11))

    print(result)
    return result


