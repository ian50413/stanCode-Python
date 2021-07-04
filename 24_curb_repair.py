"""
File: curb_repair.py
Name:
-------------------------------
This program shows how to detect red pixels
of curb and change them into gray scale, which 
is considered as an available parking space!
"""


from simpleimage import SimpleImage

THRESHOLD = 1.155


def main():
    curb_img = SimpleImage("images/curb.png")
    curb_img.show()
    for pixel in curb_img:
        avg = (pixel.red+pixel.green+pixel.blue)//3
        if pixel.red > avg * THRESHOLD:
            # curb
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    curb_img.show()


if __name__ == '__main__':
    main()
