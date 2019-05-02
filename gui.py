import Tkinter as tk
from api_interface import api_interface

class Application(tk.Frame):
    def __init__(self, master=None):
        self.interface = api_interface()

        #lists for displaying purposes
        self.recipe_ids = []
        self.recipe_list = ["RESULTS"]

        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #TOP CANVAS - DECORATIVE TEXT
        canvas_width = 240
        canvas_height = 180
        self.top_canvas = tk.Canvas(self, width=canvas_width, height=canvas_height, bg="white")
        self.top_canvas.pack(side=tk.TOP)
        self.title = self.top_canvas.create_text(canvas_width/2, canvas_height/2, 
            text="WHAT THE\n FRICK SHOULD\n I EAT? [V0.1]")
        self.question_text = self.top_canvas.create_text(canvas_width/2, canvas_height-(canvas_height/10), 
            text="Search for something!")
        #SEARCH FIELD
        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.TOP)
        #DIETARY CHOICE DROPDOWN
        diet_options = ["Please select an option", "No Dietary requirements", "Vegetarian", "Vegan", "Pescetarian", "Lacto Vegetarian", "Ovo Vegetarian"]
        diet_var = tk.StringVar(self.master)
        diet_var.set(diet_options[0])
        self.diet_dropdown = tk.OptionMenu(self.master, diet_var, *diet_options, command=self.set_diet_dropdown_value)
        self.diet_dropdown.pack(side=tk.TOP)
        #QUIT BUTTON
        self.quit_button = tk.Button(self)
        self.quit_button["text"] = "Close"
        self.quit_button["command"] = self.quit
        self.quit_button.pack(side=tk.TOP)
        #SEARCH BUTTON
        self.search_button = tk.Button(self)
        self.search_button["text"] = "Search"
        self.search_button["command"] = self.search_button_press
        self.search_button.pack(side=tk.TOP)
        #RESULTS DROPDOWN - INIT SETUP
        result_dropdown_var = tk.StringVar(self.master)
        result_dropdown_var.set(self.recipe_list[0])
        self.result_dropdown = tk.OptionMenu(self.master, result_dropdown_var, *self.recipe_list, command=self.set_result_dropdown_value)
        self.result_dropdown.pack(side=tk.TOP)
        #BOTTOM CANVAS - RESULTS DISPLAY
        #self.bottom_canvas = tk.Canvas(self, width=canvas_width*4, height=canvas_height*2, bg="grey")
        #self.bottom_canvas.pack(side=tk.BOTTOM)

    def set_diet_dropdown_value(self, value):
        #set member variable for use in 'api_interface'
        self.diet_dropdown_value = value

    def set_result_dropdown_value(self, value):
        self.selected_result = value

    def search_button_press(self):
        #get the results and update the interfaces 'search_response' object
        self.interface.get_search_results(self.entry.get(), self.diet_dropdown_value)

        #clear recipe list
        self.recipe_list = ["RESULTS"]
        #destroy previous dropdown
        self.result_dropdown.destroy()
        
        for i in range(0, len(self.interface.search_response.body['results'])):
            self.recipe_ids.append(self.interface.search_response.body['results'][i]['id'])
            #append title strings to text list
            self.recipe_list.append(self.interface.search_response.body['results'][i]['title'])

        #create new, updated dropdown
        result_dropdown_var = tk.StringVar(self.master)
        result_dropdown_var.set(self.recipe_list[0])
        self.result_dropdown = tk.OptionMenu(self.master, result_dropdown_var, *self.recipe_list)
        self.result_dropdown.pack(side=tk.TOP)

