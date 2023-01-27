from Controller.formatted_instructions import FormattedInstructions
from Controller.controller import return_random_drink
import ttkbootstrap as ttk
from Controller.format_image import FormatImage
from Controller.update_single_drink import UpdateSingleDrink


class RandomPage(ttk.Frame, UpdateSingleDrink, FormattedInstructions, FormatImage):
    """Layout for the random drink page, inherits from ttk.Frame, the mixin UpdateSingleDrink, the mixin
       FormattedInstructions, and the mixin FormatImage
    """

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
        self.image = FormatImage.format_image(self.random_data)
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
        self.instructions_text.insert(ttk.END,
                                      self.formatted_instructions(self.ingredients, self.random_data))
        self.instructions_text['state'] = 'disabled'

    def shuffle_drink(self):
        """
        shuffles the drink in the window by calling the return_random_drink method (this returns an array).
        :return: None; formats the text, and image fields in the application. The format image method is called from the
        format_image mixin which formats the jpg image. This is then returned and set in this method (it cannot be done
        outside the class). The update_single_drink method is then called, which formats the remaining widgets.
        """
        new_drink_list = return_random_drink()
        new_image = self.format_image(new_drink_list)
        self.image = new_image  # reassign image variable
        self.image_label['image'] = new_image  # set new image to the label
        self.update_single_drink(new_drink_list,
                                 self.drink_name,
                                 self.category_text,
                                 self.alcoholic_text,
                                 self.glasstype_text,
                                 self.instructions_text)
