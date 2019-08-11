#!/usr/bin/env python3

from numpy import linspace
from numpy.random import uniform

from sympy.parsing.sympy_parser import eval_expr

import numpy 

numpyDict = {a: getattr(numpy,a) for a in dir (numpy)}

def approx(f, a, b, c, d, size):
    """Approximate integral under function with a<=x<=b and c<=y<=d
    
    Args:
    
        - f (str): String format of function to approximate

        - a (float): starting value for x

        - b (float): ending value for x

        - c (float): minimum value for y

        - d (float): maximum value for y

        - size (int): number of MC draws
    """
    xs = uniform(a,b,size=size)
    ys = uniform(c,d,size=size)

    area = (d-c)*(b-a)
    under = ys < eval_expr(f, {'xs': xs}, numpyDict)

    return sum(under)/(size)*area

if __name__ == '__main__':
    from sys import argv
    f, a, b, c, d = argv[1:6]
    size = int(argv[6]) if len(argv) == 7 else 100

    a, b, c, d = map(float, (a,b,c,d))

    print('Integration {} from {} to {} with {} samples'.format(f,a,b,size))
    result = approx(f,a,b,c,d,size)
    print('approx = {}'.format(result))
