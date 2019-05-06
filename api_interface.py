#CLASS INTERFACING WITH 'SPOONACULAR' API
import unirest
import config

class api_interface():
    #dict containing api host and key
    def __init__(self):
        self.headers = {
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            "X-RapidAPI-Key": config.api_key  
        }
        self.core_address = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"
        
        #member response object containing information about search results
        self.search_response = []
        #STRUCTURE
        #   body->
            #   results->
            #       0->
            #           id
            #           title
            #       ...
            #       ...
            #       9
        #memeber response object containing recipe information - to be searched for via id
        self.recipe_response = []

    def get_search_results(self, search_term, diet_requirement):
        if diet_requirement == "No Dietary requirements":
            diet_string = ""
        else:
            diet_string = "diet=" + diet_requirement.lower()
        search_string = "recipes/search?" + diet_string + "&number=10&query=" + search_term

        self.search_response = unirest.get(self.core_address + search_string, headers=self.headers)

    def get_recipe_information(self, recipe_id):
        id_string = "recipes/" + str(recipe_id) + "/information"
        self.recipe_response = unirest.get(self.core_address + id_string, headers=self.headers)