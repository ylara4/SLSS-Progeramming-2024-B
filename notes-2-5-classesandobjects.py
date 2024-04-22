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
        self.actual_cry = "Roooooar"

        print("a pokemon is born!") 
        
def cry(self) -> str:
            """Represents the sound of a pokemon"""
            return self.actual_cry

def consume(self, item: str) -> str:
      """Pokemon consumes the item"""
      if item.lower() == "berry":
            return f"{self.name} eats the berry"
      elif item.lower() == "potion":
            return f"{self.name} feels much better after the potion!"
      else:
            return f"{self.name} batted away the {item}"
      
class Pikachu(Pokemon):
      def __init__(self, name= "Pikachu"):
            super().__init__()

self.name = __name__
self.id = 25
self.type = "Electric"

                  
def thunder(self) -> str:
      """Represents the thunder attack"""
      return f"{self.name} used Thunder"
      response = ""

    
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

    pokemon_one.actual_cry = "Pikachu"
    print(pokemon_one.actual_cry())
    pokemon_two.actual_cry = "Graaaaooor"
    print(pokemon_two.actual_cry())

    print(pokemon_one.consume("berry"))
    print(pokemon_one.consume("potion"))
    print(pokemon_one.consume("poison"))

    pikachu_one = Pikachu()
    print(pikachu_one.name, pikachu_one.type, pikachu_one.id)

    print(pikachu_one.cry())

    pass

if __name__ == "__main__":
    main()

    

