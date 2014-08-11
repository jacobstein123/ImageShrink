from PIL import Image


def compress(filename1, filename2, threshold):
    im = Image.open(filename1)
    new_image_string = ""
    pixels = list(im.getdata())
    i = 0
    focus = pixels[i]
    counter = 0
    while i < len(pixels)-1:
        i += 1
        if abs(pixels[i][0] - focus[0]) < threshold and abs(pixels[i][1] - focus[1]) < threshold and abs(pixels[i][2] - focus[2]) < threshold:
            pixels[i] = focus
    im2 = Image.new(im.mode,im.size)
    im2.putdata(pixels)
    im2.save(filename2)





