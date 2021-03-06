"""
    Functions for generating Mandelbrot Set
"""

import numpy as np

def cuadratic_function(z:complex, c:complex) -> complex:
    """
        Logistic Function : f(z, c) = z**2 + c
    """

    return z**2 + c

def get_divergence(c:complex, bound:int =4, max_steps:int =25) -> int:
    """
       Returns the iteration in which the orbit of zero for a given z starts to diverge. 
    """
    z = c
    i = 1
    
    while i<max_steps and np.sqrt(z.real**2 + z.imag**2)<bound:
        z = cuadratic_function(z, c)
        i+=1

    return i

def mandelbrot(n, max_steps=25):
    """
        Generates an image with the mandelbrot set for a given number of pixels.
    """

    mx = 2.48 / (n-1)
    my = 2.26 / (n-1)

    mapper = lambda x,y: (mx*x - 2, my*y - 1.13)
    img = np.full((n,n), 0)

    for x in range(n):
        for y in range(n):
            it = get_divergence(complex(*mapper(x,y)), max_steps=max_steps)
            img[y][x] = it

    return img