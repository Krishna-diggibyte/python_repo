import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def word_order():

    n = int(input())
    di = {}
    for _ in range(n):
        value = input()
        if value in di.keys():
            di[value] += 1
        else:
            di[value] = 1

    # print(di)
    total_no= ' '.join(str(i) for i in di.values())
    ln = str(len(di.values()))

    # logging.info(len(di.values()))
    # logging.info(total_no


    # print(type(ln))
    # print(type(total_no))
    total=ln +'\n'+ total_no
    # print(type(total))
    print(total)
    return total

