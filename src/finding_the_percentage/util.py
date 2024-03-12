import logging

logging.basicConfig(level=logging.INFO,format='%(message)s')


def find_percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = 0;
    for i in student_marks[query_name]:
        total += i;
    total /= 3
    logging.info("%.02f" % total)
    return ( total)

