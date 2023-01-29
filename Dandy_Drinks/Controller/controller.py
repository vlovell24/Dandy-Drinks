import json
import requests

"""
Controller is used as the 'Model' in our application. It's job is to query the database via functions and return data.
If an internet connection is not available, a BaseException is thrown and the value of None is returned.
"""


def return_random_drink(new_url=""):
    """
    Opens the api and gets a random drink. Once the data is recieved, it must be parsed. It is loaded into a list for
    return. The ingredients and measurements are separate values and must be forced together and then appended to the
    return list. If no param value is provided, then the random query will be run by default. If a param is provided as
    an url, it will be used for the query.
    :param: new_url; by default is set to empty string, but will take an url path
    :return: List; return_array
    :exception: Base Exception; if no internet connection is available this will be thrown and None returned
    """
    if new_url != "":
        url = new_url
    else:
        url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
    return_array = []
    ingredient_array = []
    try:
        data = requests.get(url)
        drinks = json.loads(data.text)
        for array in (drinks["drinks"]):
            return_array.extend([
                array['strDrink'],
                array['strCategory'],
                array['strAlcoholic'],
                array['strGlass'],
                array['strDrinkThumb'],
                array['strInstructions']
            ])
        for array in (drinks["drinks"]):  # map together the ingredients and measurement fields
            ingredient_array.extend([
                (array['strIngredient1'], array['strMeasure1']),
                (array['strIngredient2'], array['strMeasure2']),
                (array['strIngredient3'], array['strMeasure3']),
                (array['strIngredient4'], array['strMeasure4']),
                (array['strIngredient5'], array['strMeasure5']),
                (array['strIngredient6'], array['strMeasure6']),
                (array['strIngredient7'], array['strMeasure7']),
                (array['strIngredient8'], array['strMeasure8']),
                (array['strIngredient9'], array['strMeasure9']),
                (array['strIngredient10'], array['strMeasure10']),
                (array['strIngredient11'], array['strMeasure11']),
                (array['strIngredient12'], array['strMeasure12']),
                (array['strIngredient13'], array['strMeasure13']),
                (array['strIngredient14'], array['strMeasure14']),
                (array['strIngredient15'], array['strMeasure15'])
            ])
        # in the api, a default value of 15 ingredients and 15 measurements are provided, however not all of these are
        # used. Unused fields are marked as None, therefore after we map the ingredient/measurement entries, we will
        # want to remove the None ingredient values only. Some ingredients may have None measurement values, think lime,
        # ice cube, etc. We will filter out None measurement values later.
        for item in ingredient_array:
            if item[0] is not None:
                return_array.append(item)
    except BaseException:  # if we have no connection, return none
        return None

    return return_array


def return_categories():
    """
    Queries thecocktaildb for a list of all the drink categories. Pulls the strCategory name out of the returned data
    and appends to return_array and returns the array.
    :return:List; return_array
    :exception: BaseException thrown if no internet connection, and None returned

    """
    url = 'https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list'
    return_array = []
    try:
        data = requests.get(url)
        drinks = json.loads(data.text)
        for array in (drinks["drinks"]):
            return_array.append(array['strCategory'])
    except BaseException:  # if no connection detected
        return None

    return return_array


def return_ingredients():
    """
    Queries the database for a list of all ingredients using the variable 'url' that is set within the method. Returns
    the results of the query as a list.
    :return: list; return_array
    :exception: BaseException if no internet connection and None is returned
    """
    url = 'https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list'
    return_array = []
    try:
        data = requests.get(url)
        ingredients = json.loads(data.text)
        for array in (ingredients["drinks"]):
            return_array.append(array['strIngredient1'])
    except BaseException:
        return None
    return return_array


def return_drinks_by_ingredient(ingredient):
    """
    Queries the database for a specific drink, which is supplied as the parameter ingredient. The result of the query is
    formatted as a json object, and then the strDrink category is pulled from the data and returned. The url for the
    endpoint is stored in the method with the variable name url.
    :param ingredient: The ingredient that is being searched for. No need to force lower or upper. The api takes either.
    :return: list; return_array
    :exception: BaseException thrown if no internet is available, and None is returned.
    """
    url = f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}'
    return_array = []
    try:
        data = requests.get(url)
        drinks = json.loads(data.text)
        for array in (drinks["drinks"]):
            return_array.append(array['strDrink'])
    except BaseException:
        return None
    return return_array


def return_drinks_by_category(category):
    """
    Queries the database for a specific category, which is supplied via the parameter category. The results of the query
    are parsed into json, and then looped over. The strDrink name is appended to the return_array and returned.
    :param category: A string that is the category of drink being searched for (shot, cocktail, etc.)
    :return: list; return_array (an array of drink categories)
    :exception: BaseException thrown if no internet connection, and None returned
    """
    url = f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?c={category}'
    return_array = []
    try:
        data = requests.get(url)
        drinks = json.loads(data.text)
        for array in (drinks["drinks"]):
            return_array.append(array['strDrink'])
    except BaseException:
        return None

    return return_array


def return_drinks_by_letter(letter):
    """
    Queries the api for all drinks that start with a specific letter, provided by the parameter 'letter'. The return
    value is parsed into a json object and looped through. Each strDrink found is appended to the return_array variable
    and then returned.
    :param letter: A single 'char' being searched for
    :return: list; return_array
    :exception: BaseException thrown if no internet connection and None returned.
    """
    url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?f={letter}'
    return_array = []
    try:
        data = requests.get(url)
        drinks = json.loads(data.text)
        for array in (drinks["drinks"]):
            return_array.append(array['strDrink'])
    except BaseException:
        return None

    return return_array
