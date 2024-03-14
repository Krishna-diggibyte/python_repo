import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def no_idea():

    n , m = (input().split())
    arr = list((input().split()))
    A = set(input().split())
    B= set(input().split())
    happiness = 0
    for x in arr:
        if x in A:
            happiness+=1
        elif x in B:
            happiness -=1
    logging.info(happiness)
    return happiness
