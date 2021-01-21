"""
    Script for generating a mandelbrot set image.
    
    The Mandelbrot Set is the set of complex numbers c such that the orbit of zero 
    of the cuadratic function f(z, c) = z**2 + c remains bounded.
    
    Thus M = { c | o(0, c) is bounded}.

    The Mandelbrot Set is contained in the disk centered in zero with radius 2.

"""

import click
import matplotlib.pyplot as plt

from utils import mandelbrot

@click.command()
@click.option('--pixels', prompt='How many pixels do you want in the image?',
              help='Must be an integer')

def main(pixels):
    """
        Generate Mandelbrot Set for a given number of pixels
    """
    print(f"Generating Mandelbrot Set with {pixels} pixels...")

    img = mandelbrot(int(pixels), max_steps=100)
    plt.imshow(img, cmap="plasma")
    plt.axis("off")
    plt.savefig("mandelbrot.png")
    plt.show()

    print("Mandelbrot set successfully generated!")

if __name__ ==  "__main__":
    main()