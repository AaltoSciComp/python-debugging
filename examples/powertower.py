
def powertower(x, n):
    ''' Calculates the power tower x**x**x**x**x... where the exponentiation
    is repeated n times.
    '''

    r = 1
    for i in range(n):
        r = r**x

    return r