# ffmpeg -i original.mov -vf hue=s=0 sat.mp4
# ffmpeg -i sat.mp4 -ss 00:01:50 -t 12 cut.mp4
# ffmpeg -i cut.mp4 -vf scale=320:-1 output_320.mp4
# ffmpeg -i cut320.mp4 -r 4 -hide_banner  png/frame-%03d.png

import PIL.Image
import glob

img_flag = True
for filename in glob.glob('png/frame-*.png'):
    try:
        img = PIL.Image.open(filename)
        img_flag = True
    except:
        print(filename, f"Unable to open image {filename}");
    
    width, height = img.size
    aspect_ratio = height/width
    new_width = 320
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    
    img = img.convert('L')
    
    chars = [" ", "J", "D", "%", "*", "+", " ", "Y", "$", ",", "."]
    
    pixels = img.getdata()
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    
    new_name = filename.split('/')[1].replace('.png', '.frame')

    with open(f"frames/{new_name}", "w") as f:
        f.write(ascii_image)