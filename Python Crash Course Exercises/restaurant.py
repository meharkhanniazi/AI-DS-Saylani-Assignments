class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        '''
        This function displays name and cuisin type of 
        restaurant. It takes no argument.
        '''
        print(f"Restaurant Name:{self.restaurant_name}")
        print(f"Cuisine Type:\t{self.cuisine_type}")
        
    def open_restaurant(self):
        '''
        This function displays restaurant's opening status.
        It takes no argument.
        '''
        print(f"{self.restaurant_name} is open now.")