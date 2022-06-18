from PIL import Image, ImageEnhance

image = Image.open('/home/usr/Downloads/____.jpg')                            #image's path

new_image = image.resize((128,112))                                         #resize to gameboy's dimensions 128x112

enhancer = ImageEnhance.Contrast(new_image)
factor = 2                                                                  #increase contrast
im_output = enhancer.enhance(factor)
                                                
im_output = new_image.quantize(6)                                           #4 shades of gray

gameboy = im_output.resize((500,500))                                       #resize 600x600
gameboy.show()