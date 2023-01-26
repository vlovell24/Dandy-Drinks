import io
import urllib.request
from Controller.controller import return_random_drink
import ttkbootstrap as ttk
from PIL import Image, ImageTk


class RandomPage(ttk.Frame):
    """Layout for the random drink page"""

    def __init__(self, parent, random_data, home_page):  # home page is a method to go back to the home page
        ttk.Frame.__init__(self, parent)
        self.homepage = home_page
        self.random_data = random_data  # the entire drink object
        self.ingredients = random_data[6:]  # only the ingredients/measurements from the drink object
        # ------------------------------------------------FRAME FOR TOP BUTTON AND DRINK NAME---------------------------
        self.top_frame = ttk.Frame(self)
        self.top_frame.grid(row=0, column=0, sticky='nsew')
        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.columnconfigure(1, weight=1)
        self.top_frame.columnconfigure(2, weight=1)
        # ----------------------------------------------------SHUFFLE BUTTON--------------------------------------------
        self.shuffle_button = ttk.Button(
            self.top_frame,
            text="Shuffle New Random Drink",
            bootstyle="info",
            command=lambda: self.shuffle_drink()
        )
        self.shuffle_button.grid(row=0, column=0, sticky='w')
        # -----------------------------------------------------HOME BUTTON----------------------------------------------
        self.home_button = ttk.Button(
            self.top_frame,
            text="Home",
            bootstyle="dark",
            command=self.homepage
        )
        self.home_button.grid(row=0, column=2, sticky='e')
        # ----------------------------------------------------------DRINK NAME------------------------------------------
        self.drink_name = ttk.Label(
            self.top_frame,
            text=random_data[0],
            font=("Comic Sans MS", 20, "bold"),
            bootstyle="info"
        )
        self.drink_name.grid(row=0, column=1, sticky='ew')
        # ----------------------------------------------------------DRINK IMAGE-----------------------------------------
        self.image = self.format_image(self.random_data)
        self.image_label = ttk.Label(
            self,
            image=self.image,
            bootstyle='inverse-secondary',
            anchor='center'
        )
        self.image_label.grid(row=1, column=0, sticky='nsew', pady=20, ipadx=10, ipady=10)
        # -----------------------------------------------------BOTTOM FRAME---------------------------------------------
        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.grid(row=2, column=0, sticky='nsew')
        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(1, weight=1)
        self.bottom_frame.rowconfigure(0, weight=1)
        # ------------------------------------------------LEFT AND RIGHT FRAMES TO HOLD CONTENT-------------------------
        self.left_frame = ttk.Frame(self.bottom_frame)
        self.right_frame = ttk.Frame(self.bottom_frame)
        self.left_frame.grid(row=0, column=0)
        self.right_frame.grid(row=0, column=1)
        # -----------------------------------------------LEFT SIDE CATEGORY LABELFRAME----------------------------------
        self.drink_category = ttk.LabelFrame(
            self.left_frame,
            text="Drink Category",
            bootstyle='info'
        )
        self.drink_category.grid(row=0, column=0, padx=(0, 20))

        # -----------------------------------------------------CATEGORY TEXT------------------------------------------
        self.category_text = ttk.Label(
            self.drink_category,
            text=random_data[1],
            font=("Comic Sans MS", 12),
            width=25
        )
        self.category_text.pack(fill='x', side='left', expand=True)
        # -----------------------------------------------------LEFT ALCOHOLIC LABELFRAME--------------------------------
        self.alcoholic = ttk.LabelFrame(
            self.left_frame,
            text="Alcoholic or Non",
            bootstyle='info'
        )
        self.alcoholic.grid(row=1, column=0, padx=(0, 20), pady=5)
        # ------------------------------------------------------ALCOHOLIC LABELFRAME TEXT-------------------------------
        self.alcoholic_text = ttk.Label(
            self.alcoholic,
            text=random_data[2],
            font=("Comic Sans MS", 12),
            width=25
        )
        self.alcoholic_text.pack(fill='x', side='left', expand=True)
        # --------------------------------------------------------GLASS TYPE LABELFRAME---------------------------------
        self.glasstype = ttk.LabelFrame(
            self.left_frame,
            text="Glass Type",
            bootstyle='info'
        )
        self.glasstype.grid(row=2, column=0, padx=(0, 20), pady=(0, 5))
        # -----------------------------------------------------GLASS TYPE TEXT------------------------------------------
        self.glasstype_text = ttk.Label(
            self.glasstype,
            text=random_data[3],
            font=("Comic Sans MS", 12),
            width=25
        )
        self.glasstype_text.pack(fill='x', side='left', expand=True)
        # ------------------------------------------------------RIGHT SIDE INFO-----------------------------------------
        self.instructions = ttk.LabelFrame(
            self.right_frame,
            text="Instructions",
            bootstyle='info'
        )
        self.instructions.grid(row=0, column=1)

        self.instructions_text = ttk.Text(
            self.instructions,
            wrap="word",
            width=75,
            height=10
        )
        self.instructions_text.pack(fill='both', side='left', expand=True)
        self.instructions_text.insert(ttk.END, self.formatted_data_for_instructions_field(self.ingredients, self.random_data))
        self.instructions_text['state'] = 'disabled'

    def shuffle_drink(self):
        """
        shuffles the drink in the window by calling the return_random_drink method (this returns an array). We then take
        the new drink and separate the ingredients portion of the object. With these two arrays, we can then set the
        labels and image in the application to the new values. The new image must be run through the format_image method
        before it can be assigned to the image label. We also need to run the new_drink_list and ingredients through the
        formatted_data_for_instructions_field method that will format the return data correctly to place into the text
        area in the application.
        :return: None; formats the text, and image fields in the application.
        """
        url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
        new_drink_list = return_random_drink(url)
        ingredients = new_drink_list[6:]
        # change drink name
        self.drink_name['text'] = new_drink_list[0]
        new_image = self.format_image(new_drink_list)
        # now assign the image to the image label
        self.image = new_image  # reassign image variable
        self.image_label['image'] = new_image  # set new image to the label
        # assign category
        self.category_text['text'] = new_drink_list[1]
        # assign alcoholic/non
        self.alcoholic_text['text'] = new_drink_list[2]
        # assign glass type
        self.glasstype_text['text'] = new_drink_list[3]
        # assign instructions including the ingredients/measurements
        self.instructions_text['state'] = 'normal'  # enable the text field
        self.instructions_text.delete(1.0, ttk.END)  # delete the contents
        new_instructions = self.formatted_data_for_instructions_field(ingredients, new_drink_list)
        self.instructions_text.insert(ttk.END, new_instructions)  # replace the contents
        self.instructions_text['state'] = 'disabled'  # disable the text field again

    def format_image(self, data_array):
        """formats and returns an image object(only for jpg, png values do not need the io.BytesIO).
        """
        with urllib.request.urlopen(data_array[4]) as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        image_resized = image.resize((300, 300), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image_resized)
        return image

    def formatted_data_for_instructions_field(self, ingredient_list, data_list):
        """
        Takes in the ingredient list and the data list. For every two items in the ingredient list, it separates them by
        tabs. Every third item is put on a new line. These items are appended to the formatted_string variable. After
        all the ingredients are formatted and appended to the string, the instructions are then added to the string.
        The final string is looped through one additional time to remove any None values in the ingredient measurement
        section. The string is then returned to be placed in the label.
        :param ingredient_list: list of ingredients and measurements
        :param data_list: entire drink array; we need index 5 for instructions
        :return: none_removed; a formatted string
        """
        formatted_string = ""
        for index, ingredient in enumerate(ingredient_list):
            if index % 2 == 0:
                formatted_string += f"{ingredient[0]}: {ingredient[1]}\t\t\t\t"
            else:
                formatted_string += f"{ingredient[0]}: {ingredient[1]}\n"

        formatted_string += f"\n\n{data_list[5]}"
        # remove the None values if found in the measurement section. Some ingredients do not have a measurement
        none_removed = formatted_string.replace("None", "")
        return none_removed


