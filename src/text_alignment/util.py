
import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')


def print_pattern():

    n = int(input())
    c = 'H'
    result=""
    # Top Cone
    for i in range(1, n + 1):
        # logging.info((c * ((i * 2) - 1)).center(n * 2 - 1))
        result+=(c * ((i * 2) - 1)).center(n * 2 - 1)+'\n'

    # top Piller
    for i in range(n + 1):
        # logging.info((c * n).center(n * 2) + (c * n).center(n * 6))
        result+=(c * n).center(n * 2) + (c * n).center(n * 6)+'\n'

    # Middle Belt
    for i in range(int((n + 1) / 2)):
        # logging.info((c * n * 5).center(n * 6))
        result+=(c * n * 5).center(n * 6)+'\n'

    # bottom Piller
    for i in range(n + 1):
        # logging.info((c * n).center(n * 2) + (c * n).center(n * 6))
        result+=(c * n).center(n * 2) + (c * n).center(n * 6)+'\n'

    # bottom Cone

    for i in range(n, 0, -1):
        # logging.info((c * 0).center(n * 4) + (c * ((i * 2) - 1)).center(n * 2 - 1))
        result+=(c * 0).center(n * 4) + (c * ((i * 2) - 1)).center(n * 2 - 1)+'\n'

    logging.info(result)
    return result