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


    #
    # arr1_str = np.array2string(n_f, formatter={'float_kind': lambda x: "%.0f" % x})
    #
    # print(arr1_str)
    # print(n_f)
    #
    # combined_string ='['+ ','.join(map(str, n_f)) + ']\n[' + ','.join(map(str, n_c)) + ']\n[' + ','.join(map(str, n_r))+']'
    #
    # print(combined_string)
    # return combined_string
    # return n_c+" "+n_f+" "+n_r
    #
    # print(n_c)
    # ans = ' '.join(map(str, n))
    # logging.info({},{},n_f,n_c)
    # logging.info(n_c)
    # logging.info(n_r)
    #
    #
    # ans= (np.floor(new_arr),'\n'+np.ceil(new_arr),'\n'+np.rint(new_arr))
    # return ans
