from util import find_runner_up

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_list = (list(arr))
    new_list.sort()
    find_runner_up(new_list)