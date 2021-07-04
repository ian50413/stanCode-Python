"""
Implements some functionality of a Photoshop program!

Remember that the SimpleImage properties include:
    pixel.x pixel.y pixel.red pixel.green pixel.blue
    image.width image.height
where each SimpleImage is made up of many pixels.
"""

from simpleimage import SimpleImage


def main():
    """
    Run your desired photoshop functions here.
    You should save the return value of the image and then
    call .show() to visualize the output of your program.
    """
    img = SimpleImage('images/stanford.jpg')
    img.show()

    updated_img = jerry_channel(img)
    updated_img.show()


def red_channel(img):
    """
    remove all blue and green colors from the photo to enhance
    the red channel of its pixels (the R in RGB).
    ---------------------------------------------------
    :param img: (SimpleImage) the original image
    :return: The updated image with all pixels turning red
    """
    for pixel in img:
        pixel.green = 0
        pixel.blue = 0
    return img



def green_channel(img):

    for pixel in img:
        pixel.red = 0
        pixel.blue = 0
    return img


def blue_channel(img):

    for pixel in img:
        pixel.red = 0
        pixel.green = 0
    return img


def jerry_channel(img):

    for pixel in img:
        pixel.red -= 20
        pixel.green //= 2
        pixel.blue *= 1.5
    return img


if __name__ == '__main__':
    main()
