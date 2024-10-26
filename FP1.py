# This Python program creates a Mad Libs game where the player is prompted to enter specific words, which are then inserted into a pre-defined story template. The player is asked to provide various types of words such as a large object, multiple large objects, an adjective, a body part, a restaurant name, and two types of food. The game displays a message with instructions and then takes inputs for each required word. These inputs are stored in variables and later used to populate a story template. Finally, the completed story is printed with the player's inputs in the appropriate places.

print("Welcome to Mad Libs! Please provide the words as prompted to complete your story.")

large_object = input("Enter a large object: ")
large_objects_plural = input("Enter multiple large objects (plural): ")
adjective = input("Enter an adjective: ")
body_part = input("Enter a body part: ")
restaurant = input("Enter the name of a restaurant: ")
first_food = input("Enter a type of food: ")
second_food = input("Enter another type of food: ")

story = (
    f"I’ve had a very {adjective} day.\n"
    f"This morning, I dropped a box of {large_objects_plural} on my {body_part}.\n"
    f"Then, at lunch, I went to {restaurant} for their delicious {first_food},\n"
    f"But the waiter brought me {second_food}, which I was not hungry for.\n"
    f"Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."
)

print("\nHere is your story:")
print(story)
