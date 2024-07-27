from PIL import Image as img
import numpy as np


def map(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def mod(z):
    return np.sqrt(z[0]*z[0] + z[1]*z[1])


def main():

    width, height = 36000, 36000
    image = img.new('RGBA', (width, height), (0, 0, 0))
    pixels = image.load()
    for x in range(0, width):
        for y in range(0, height):

            a = map(x, 0, width, -2, 2)
            b = map(y, 0, height, -2, 2)

            ca = a
            cb = b

            for n in range(100):
                if mod((a, b)) > 2:
                    break

                aa = a*a - b*b
                bb = 2*a*b

                a = aa + ca
                b = bb + cb

            if n == 99:
                pixels[x, y] = (0, 0, 0)
            else:
                color = int(map(n, 0, 100, 0, 255))
                pixels[x, y] = (color, color, color)

    image.save('mandelbrot_set.png', format='PNG')


if __name__ == '__main__':
    main()




