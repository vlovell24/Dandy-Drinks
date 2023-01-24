from tkinter import BOTH, YES
from View.home_button_frame import MainButtonGroup
from Controller.controller import return_random_drink
import ttkbootstrap as ttk
from Images import LOGO
from View.title_bar import TitleBar
from View.gif import AnimatedGif
from View.home_text import HomeText
from View.random_page import RandomPage

class Application(ttk.Window):
    # -------------------------------SET SINGLETON FOR ONLY ONE INSTANCE OF APP AT ONE TIME-----------------------------
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False
        return cls._instance

    # ------------------------------------CONSTRUCTOR-------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # --------------------------------SET THEME AND DISABLE CLOSE BUTTON--------------------------------------------
        self.style.theme_use('united')
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        # ------------------------------------------TITLE AND LOGO------------------------------------------------------
        self.title("Dandy Drinks")
        self.logo = ttk.PhotoImage(file=LOGO)
        self.iconphoto(False, self.logo)
        # ----------------------------------CENTER SCREEN, SET SIZE, SET RESIZEABLE-------------------------------------
        self.w = 825
        self.h = 720
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        self.x = (self.ws / 2) - (self.w / 2)
        self.y = (self.hs / 2) - (self.h / 2)
        self.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.resizable(False, False)
        # -------------------------------------TITLE BAR----------------------------------------------------------------
        self.title_bar = TitleBar(self)
        self.title_bar.pack(fill='x')
        # --------------------------------------GIF---------------------------------------------------------------------
        self.gif = AnimatedGif(self)
        self.gif.pack()
        # --------------------------------------HOME TEXT---------------------------------------------------------------
        self.home_text = HomeText(self)
        self.home_text.pack()
        # --------------------------------------- BOTTOM BUTTONS AND IMAGES---------------------------------------------
        self.bottom_section = MainButtonGroup(self, self.gif, self.home_text, lambda: self.destroy_widgets())
        self.bottom_section.pack(fill='x')

    def destroy_widgets(self):
        # get the random drink data that we want to append to the application window
        random_data = return_random_drink()
        if random_data: # if we can connect to the interwebz
            # destroy widgets on application page
            self.home_text.destroy()
            self.gif.destroy()
            self.bottom_section.destroy()
            # create random page
            self.create_random_widgets(random_data)
        else:  # if there was a connection error
            return


    def create_random_widgets(self, data):
        RandomPage(self, data).pack()


    def on_close(self):
        """Use to create custom close later"""
        self.destroy()
