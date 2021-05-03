import sys
from PIL import Image, ImageFilter
try:
    tigerpic = Image.open("tigerpic.jpeg")
except IOError:
    print("Image didn't load")
tigerpic.show()
# Print the Tiger Pic information (size and format)
print(tigerpic.size)
print(tigerpic.format)
