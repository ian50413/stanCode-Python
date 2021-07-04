"""
File: flip_horizontally.py
Name: 
------------------------------------
This program shows how to create an empty SimpleImage
as well as making a mirrored image of poppy.png by
inserting old pixels into the empty one 
"""


from simpleimage import SimpleImage


def main():
    old_img = SimpleImage("images/poppy.png")
    blank_img = SimpleImage.blank(old_img.width*2, old_img.height)
    for x in range(old_img.width):
        for y in range(old_img.height):
            # Colored pixel
            old_pixel = old_img.get_pixel(x, y)
            # Empty Pixel 1
            new_pixel = blank_img.get_pixel(x, y)
            # Empty Pixel 2
            new_pixel2 = blank_img.get_pixel(blank_img.width-1-x, y)
            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue
            new_pixel2.red = old_pixel.red
            new_pixel2.green = old_pixel.green
            new_pixel2.blue = old_pixel.blue
    blank_img.show()


if __name__ == '__main__':
    main()
