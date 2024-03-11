def find_runner_up(new_list):
    mmax = new_list[1]
    bmax = new_list[0]

    for i in new_list:
        if (i > mmax):
            bmax = mmax
            mmax = i;
    print(bmax)

