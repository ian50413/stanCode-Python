"""
File: photoshop.py
Name: Jerry Liao 2020/07
-------------------------------------
This program replaces the background of jerry.jpeg
with wave.jpeg, providing students some insights into
photoshop techniques 
"""


from simpleimage import SimpleImage


# Constants
THRESHOLD = 1.3     # Controls the threshold of detecting green screen pixel
BLACK_PIXEL = 120   # Controls the upper bound for black pixel


def combine(back, me):
    """
    : param1 back: SimpleImage, the background image
    : param2 ma: SimpleImage, green screen figure image
    : return me: SimpleImage, me image with the green screen pixels replaced by pixels of back
    """
    for y in range(back.height):
        for x in range(back.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            if pixel_me.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = back.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me


def main():
    """
    This function conducts green screen replacement
    that is able to photoshop a person onto any background
    """
    fg = SimpleImage('images/jerry.jpeg')
    bg = SimpleImage('images/wave.jpeg')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()


if __name__ == '__main__':
    main()
