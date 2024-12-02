# Step 1: Define the base class
class Animal:
    def __init__(self, name):
        self.name = name  # Common attribute
    
    def speak(self):
        print("The animal makes a sound.")

# Step 2: Define the first derived class (Dog)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed  # Specific attribute for Dog
    
    def speak(self):  # Overriding the speak method
        print(f"{self.name} barks.")

# Step 3: Define the second derived class (Cat)
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the parent class constructor
        self.color = color  # Specific attribute for Cat
    
    def speak(self):  # Overriding the speak method
        print(f"{self.name} meows.")

# Create instances of Dog and Cat
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")

# Access the speak method from both classes
dog.speak()  # Output: Buddy barks.
cat.speak()  # Output: Whiskers meows.
