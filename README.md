## :wine_glass: DANDY DRINKS :cocktail:

### :eyes: About
 Dandy drinks is a desktop application that uses :tropical_drink: thecocktaildb.com api to create a 
fun application for anything drink related. Generate random drinks :beer:, search for drinks 
by glass type :tumbler_glass:, alcohol :beers:, alcoholic/non-alcoholic :bubble_tea:, or any ingredients. :question: 

### :question: Why?
I created this as a beginner lesson in accessing api's, retrieving data and making a fully 
dynamic desktop application with Python and Tkinter. 

### Lets's Begin:

The application opens to a 'home page' screen with a banner image near the top of the page,
and four buttons at the bottom of the page labeled as:
- :mag: Search By Drink Categories
- :mag: Select Random
- :mag: Search By First Letter
- :mag: Search By Ingredient

<p float="left">
<img src="readme_images/dandy_home.png" alt="home page" style="width: 500px;"/>
</p>

### Select Random Button

<p float="left">
<img src="readme_images/button_random.png" alt="random button" style="width: 200px;"/>
</p>

When clicked, the Select Random button opens a new 'page' in the application that displays a
random drink brought back from the api. 

<p float="left">
<img src="readme_images/dandy_random.png" alt="random page" style="width: 500px;"/>
</p>

The random page displays the following information:
- :wine_glass: The name of the drink as a title at the top of the page
- :twisted_rightwards_arrows: A Shuffle New Random Drink Button at the top of the page
- :house: A Home Button at the top of the page
- :tropical_drink: An image of the drink 
- Fields for:
  - Drink Category
  - Alcoholic or Non-Alcoholic
  - Glass Type
  - Instructions for making the drink including ingredients and measurements

Clicking on the :twisted_rightwards_arrows: Shuffle New Random Drink Button will return a new random drink.
Clicking on the :house: Home button will return the user to the Home page of the application.

<p float="left">
<img src="readme_images/dandy_shuffle.png" alt="random shuffle" style="width: 500px;"/>
</p>
  
### SEARCH BY DRINK CATEGORIES

<p float="left">
<img src="readme_images/dandy_category.png" alt="category page" style="width: 500px;"/>
</p>

The category page contains the following:
- A drink category dropdown
- A drink dropdown
- A home button

The page is fully dynamic, therefore when a new drink category is selected, the default first
value is shown in the dropdown below, and the page changes to that drink. When a new drink is
selected, the page also changes to the newly selected drink. The user may go back to the home page at any time
by clicking the home button.

### SEARCH BY FIRST LETTER

<p float="left">
<img src="readme_images/search_alphabetical.png" alt="alphabet page" style="width: 500px;"/>
</p>

The search by first letter page opens a new application page with two dropdowns:
- Select a Letter (alphabetical dropdown)
- Select a Drink (Select drink)
This page is also fully dynamic, and when a letter is selected, the select drink dropdown will query the api for the 
letter selected, and return all drinks starting with that letter, in the select a drink dropdown. When a drink is selected
the page will change with that drinks values.

### SEARCH BY INGREDIENT

<p float="left">
<img src="readme_images/search_ingredient.png" alt="alphabet page" style="width: 500px;"/>
</p>

The search by ingredient page opens a new application page with two dropdowns:
- Select a Ingredient
- Select a Drink
This page is fully dynamic and when an ingredient is selected, the select drink dropdown will query the api and change the
second select drink dropdown. Once a new drink is selected from this dropdown, the page will update with the new values. 
## Additional Notes :ledger:
- :computer: The GUI for this application is made with Tkinter and TTKBootstrap
- :art: The theme used from tkinter is 'United'
- :globe_with_meridians: This is a desktop application, but an internet connection is required to query the api
- :signal_strength: The api is thecocktaildb.com


