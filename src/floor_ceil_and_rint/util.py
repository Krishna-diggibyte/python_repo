import numpy as np
import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')
def floor_ceil():

    np.set_printoptions(legacy='1.13')
    n=input()

    new_arr=list(float(i) for i in n.split(' '))

    # print(np.floor(new_arr),np.ceil(new_arr),np.rint(new_arr), sep='\n')

    n_f=np.floor(new_arr)
    n_c=np.ceil(new_arr)
    n_r=np.rint(new_arr)

    # logging.info(n_f)
    # logging.info(n_c)
    # logging.info(n_r)
    logging.info("%s \n%s \n%s \n",n_f,n_c,n_r)
    return (n_f,n_c,n_r)


    return  result

