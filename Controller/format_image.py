import io
import urllib.request
from PIL import Image, ImageTk


class FormatImage:
    """A utility class/mixin for formatting the .jpg images that come back from the api"""
    @staticmethod
    def format_image(data):
        with urllib.request.urlopen(data[4]) as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        image_resized = image.resize((300, 300), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image_resized)
        return image
