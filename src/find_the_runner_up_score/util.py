import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')
def find_runner_up():
    n = int(input())
    arr = map(int, input().split())
    new_list = (list(arr))
    new_list.sort()
    mmax = new_list[1]
    bmax = new_list[0]

    for i in new_list:
        if (i > mmax):
            bmax = mmax
            mmax = i;
    logging.info(bmax)
    return bmax


