def approximate_pi(n_terms):
    dis = 0
    for i in range(n_terms):
        dis += ((-1)**i)/(2*i + 1)
    pi = dis*4
    return pi
