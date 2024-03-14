import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def print_formatted():
    n = int(input())
    width = len(bin(n)[2:])
    result=""
    for i in range(1, n+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        # print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

        newline=(deci.rjust(width)+' '+octa.rjust(width)+' '+hexa.rjust(width)+' '+bina.rjust(width))
        # logging.info(newline)
        result+=newline+'\n'
    logging.info(result)
    return result
