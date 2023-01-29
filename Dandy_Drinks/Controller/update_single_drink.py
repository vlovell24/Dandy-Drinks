from tkinter import END
from Dandy_Drinks.Controller.formatted_instructions import FormattedInstructions

"""
The UpdateSingleDrink class is used to change the widget values for one drink. Each page has an end result of returning
a single updated drink, therefore this class is a helper/utility/mixin class that may be used as multi-inheritance or 
as an import. Either is fine. This class updates the drink name, category, alcoholic or non, glass type, and
instructions for a drink. Because the instructions widget is a Text widget, and it is disabled from modification, it 
must first be enabled, the original values deleted, and then updated with the new values. Then it must be disabled again
"""


class UpdateSingleDrink:
    """
    Used to update a single drinks widget values.
    :return: None; updates widget values
    :exception: IndexError, if index out of range, returns None
    """

    @staticmethod
    def update_single_drink(data, drink_name, category, alcoholic, glass, instructions):
        try:
            ingredients = data[6:]
            drink_name['text'] = data[0]
            category['text'] = data[1]
            alcoholic['text'] = data[2]
            glass['text'] = data[3]
            instructions['state'] = 'normal'
            instructions.delete(1.0, END)
            new_instructions = FormattedInstructions.formatted_instructions(ingredients, data)
            instructions.insert(END, new_instructions)
            instructions['state'] = 'disabled'
        except IndexError:
            return None
