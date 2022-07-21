import numpy
from PIL import Image
import datetime
import random
import piexif
import piexif.helper

# Generate random list with datetime
dt = datetime.datetime(2010, 12, 1)
end = datetime.datetime(2010, 12, 30, 23, 59, 59)
step = datetime.timedelta(seconds=5)
generated_range = []
while dt < end:
    generated_range.append(dt.strftime("%Y:%m:%d %H:%M:%S"))
    dt += step

# lyrics
lyrics_list = []
with open('lyrics') as lyrics_file:
    lyrics_list = lyrics_file.read().split('\n')
    lyrics_list = [x for x in lyrics_list if x]

# Get random values from this list
random_list = []
for i in range(100):
    random_list.append(random.choice(generated_range))

# Generate images
for n in range(100):
    filename = 'images/out%000d.jpg' % n
    a = numpy.random.rand(30, 30, 3) * 255
    im_out = Image.open('class.jpg')
    im_out.save(filename)
    new_date = random_list[n]
    exif_dict = piexif.load(filename)

    exif_dict['Exif'][piexif.ExifIFD.UserComment] = str.encode(
        random.choice(lyrics_list))
    if (new_date == min(random_list)):
        exif_dict['Exif'][piexif.ExifIFD.UserComment] = str.encode(
            "Sa Srbima ne smije e inat da se tera. Izgubićeš jato crnih bombardera")
        print(filename)
    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, filename)
