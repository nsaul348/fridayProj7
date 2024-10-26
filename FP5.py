# This Python program defines five functions to change the color of text using ANSI color codes. Each function takes a string as input and returns the text formatted in a specific color, such as red, blue, green, yellow, or brown. The program allows the user to select a color and input text to display in that color. An optional feature includes a sixth function that randomly selects a color from the five defined colors. A loop is added to allow users to color multiple pieces of text in one session, with an option for custom ANSI color codes for additional color experimentation.

import random

# Define functions for each color, using ANSI escape codes to color the text
def red_text(text):
    return f"\033[31m{text}\033[0m"

def blue_text(text):
    return f"\033[34m{text}\033[0m"

def green_text(text):
    return f"\033[32m{text}\033[0m"

def yellow_text(text):
    return f"\033[33m{text}\033[0m"

def brown_text(text):
    return f"\033[36m{text}\033[0m"

# Define a function to randomly select a color function
def random_color_text(text):
    color_function = random.choice([red_text, blue_text, green_text, yellow_text, brown_text])
    return color_function(text)

# Main program logic
print("Welcome to the Colorful Text Program!")

while True:
    # Prompt the user to choose a color or select a random one
    color_choice = input("Choose a color (red, blue, green, yellow, brown, random, or custom) or type 'quit' to exit: ").strip().lower()
    
    if color_choice == "quit":
        print("Goodbye! Thank you for using the Colorful Text Program!")
        break
    
    text = input("Enter the text you'd like to color: ")
    
    # Display the text in the chosen color or custom color if provided
    if color_choice == "red":
        print(red_text(text))
    elif color_choice == "blue":
        print(blue_text(text))
    elif color_choice == "green":
        print(green_text(text))
    elif color_choice == "yellow":
        print(yellow_text(text))
    elif color_choice == "brown":
        print(brown_text(text))
    elif color_choice == "random":
        print(random_color_text(text))
    elif color_choice == "custom":
        custom_code = input("Enter a custom ANSI color code (e.g., 31 for red, 32 for green): ")
        print(f"\033[{custom_code}m{text}\033[0m")
    else:
        print("Invalid choice. Please choose a valid color option.")

print("Program ended.")
