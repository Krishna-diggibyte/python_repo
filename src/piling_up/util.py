import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')
def pilling_up():
    result=""
    T = int(input())
    for i in range(T):
        n=int(input())
        blocks=list(map(int,input().split()))
        new_list=[]
        while len(blocks)>0:
            if blocks[-1]>blocks[0]:
                new_list.append(blocks.pop(-1))
            else:
                new_list.append(blocks.pop(0))
        test_list=new_list.copy()
        new_list.sort(reverse=True)
        #print(b)
        if new_list==test_list:
            logging.info('Yes')
            result += 'Yes'+'\n'
        else:
            logging.info('No')
            result += 'No'+'\n'
    return result
