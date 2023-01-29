import io
import urllib.request
from PIL import Image, ImageTk

"""
FormatImage is used as a utility/helper/mixin class. It is used to format/parse a .jpg file correctly. The database that
we are querying returns a .jpg image and not a .png, therefore we must format it for reading by tkinter.
"""


class FormatImage:
    """
    urllib is used to open the url path and read the image as bytes. The image is resized, antialias is applied, and the
     image is finally opened via ImageTk.PhotoImage. It is then returned.
     :exception: BaseException thrown if no internet connection, and None is returned.
    """
    @staticmethod
    def format_image(data):
        try:
            with urllib.request.urlopen(data[4]) as u:
                raw_data = u.read()
            image = Image.open(io.BytesIO(raw_data))
            image_resized = image.resize((300, 300), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image_resized)
            return image
        except BaseException:
            return None
