"""
File: img_processing_2.py
Name:
-------------------------------
This file contains 2 image processing algorithms:
(1.) left_half_darken
(2.) gray_scale
"""


from simpleimage import SimpleImage


def main():
    """
    This file contains 2 image processing algorithms:
    left_half_darken and gray_scale
    """
    img = SimpleImage('images/stop.png')
    img.show()

    # half_dark_img = left_half_darken('images/stop.png')
    # half_dark_img.show()

    # special_img = special_darken('images/stop.png')
    # special_img.show()

    gray_scale_img = gray_scale('images/stop.png')
    gray_scale_img.show()


def special_darken(filename):
    img = SimpleImage(filename)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x,y)
            if x < img.width // 2:
                if y < img.height // 2:
                    pixel.red //= 2
                    pixel.green //= 2
                    pixel.blue //= 2
            if x >= img.width // 2:
                if y >= img.height // 2:
                    pixel.red //= 2
                    pixel.green //= 2
                    pixel.blue //= 2
    return img


def left_half_darken(filename):
    """
    :param filename: str, the file path of the original image
    :return img: The image with half horizontal area darken
    """
    img = SimpleImage(filename)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x,y)
            if x < img.width//2:
                #darken
                pixel.red //= 2
                pixel.green //= 2
                pixel.blue //= 2
    return img


def gray_scale(filename):
    """
    :param filename: str, the file path of the
                          original colored image
    :return: Gray scaled image
    """
    original_img = SimpleImage(filename)
    for pixel in original_img:
        avg = (pixel.red+pixel.green+pixel.blue)//3
        pixel.red = avg
        pixel.green = avg
        pixel.blue = avg
    return original_img


if __name__ == '__main__':
    main()
