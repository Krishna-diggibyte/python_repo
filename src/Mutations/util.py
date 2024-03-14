import logging

logging.basicConfig(level=logging.INFO,format='%(message)s')
def mutate_string():
    string = input()
    position, character = input().split()
    l = list(string)
    l[int(position)] = character
    string = ''.join(l)
    logging.info(string)
    return string