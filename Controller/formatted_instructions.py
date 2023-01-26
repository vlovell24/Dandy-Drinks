

class FormattedInstructions:
    """A utility class for formatting the instructions field text correctly"""
    @staticmethod
    def formatted_instructions(ingredients, data):
        formatted_instructions = ""
        for index, ingredient in enumerate(ingredients):
            if index % 2 == 0:
                formatted_instructions += f'{ingredient[0]}: {ingredient[1]}\t\t\t\t'
            else:
                formatted_instructions += f'{ingredient[0]}: {ingredient[1]}\n'
        formatted_instructions += f"\n\n{data[5]}"
        # remove the None values if found in the measurement section. Some ingredients do not have a measurement
        none_removed = formatted_instructions.replace("None", "")
        return none_removed
