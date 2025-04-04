# Base class: Superhero
class Superhero:
    def __init__(self, name, power, origin):
        # Constructor to initialize attributes
        self.name = name
        self.power = power
        self.origin = origin
    
    # Method to display superhero info
    def display_info(self):
        return f"Superhero Name: {self.name}\nPower: {self.power}\nOrigin: {self.origin}"
    
    # Method to perform an action
    def use_power(self):
        return f"{self.name} is using their power: {self.power}!"

# Subclass: FlyingSuperhero (Inheritance layer)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        # Call the parent class constructor
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed  # Add unique attribute
    
    # Polymorphism: Override the display_info method
    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info}\nFlight Speed: {self.flight_speed} km/h"
    
    # Unique method for FlyingSuperhero
    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} km/h!"

# demo for encapsulation: Protect a secret identity
class SecretIdentitySuperhero(Superhero):
    def __init__(self, name, power, origin, secret_identity):
        super().__init__(name, power, origin)
        self.__secret_identity = secret_identity  # Private attribute
    
    def reveal_identity(self):
        return f"The secret identity of {self.name} is {self.__secret_identity}!"

# Create objects of Superhero and FlyingSuperhero
hero1 = Superhero("Thunderbolt", "Lightning Strike", "Earth")
hero2 = FlyingSuperhero("SkyFlare", "Fireball Blast", "Mars", 500)
hero3 = SecretIdentitySuperhero("ShadowKnight", "Invisibility", "Moon", "John Doe")

# Display infor about the superheroes
print(hero1.display_info())
print(hero1.use_power())

print(hero2.display_info())
print(hero2.use_power())
print(hero2.fly())

print(hero3.display_info())
print(hero3.use_power())
print(hero3.reveal_identity())
