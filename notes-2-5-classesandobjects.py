# Classes and objects
# Yeshua Lara
# April 15

# Big Ideas:
# Classes are things in Python that allow us to bundle data and functions together.
# Objects are the actual representation of the classes in our Python scripts.

# Terminology:
# Properties - Properties are the data that defines a particular class.
# Methods - Methods are the functions that define what a particular class can do.

# create a class that represents a pokemon
class Pokemon: 
    def __init__(self):
        self.name = ""
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "Normal"
def main():
    pokemon_one = Pokemon()
    print(pokemon_one.name)
    print(pokemon_one.type)
    pokemon_one.name = "Pikachu"
    pokemon_one.type = "Electric"
    pokemon_one.id = 25
    print(pokemon_one.name)
    print(pokemon_one.type)
    pass
      

            # TODO: Create something 'Squirtle'-like
    #  - Create a new Pokemon object
    #      - Store this in variable pokemon_two
    #  - Squirtle's Pokedex id is 4
    #  - Squirtle's type is Water
    # To test, print out all of squirtle's properties
            
    pokemon_two = Pokemon()
    print(pokemon_two.name)
    print(pokemon_two.type)
    pokemon_two.name = "Squirtle"
    pokemon_two.type = "Water"
    pokemon_two.id = 4
    print(pokemon_two.name)
    print(pokemon_two.type)
    pass

if __name__ == "__main__":
    main()

