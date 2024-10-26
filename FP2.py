# This Python program generates random lottery numbers for a PowerBall ticket, where five numbers are selected from 1 to 69, and one final "PowerBall" number is chosen from 1 to 26. The program first greets the user, explaining that it will generate random lottery numbers. Using the `randint` function from the `random` module, it creates five random numbers between 1 and 69 and one additional random number between 1 and 26. These numbers are stored in variables and then printed in a single line with one space between the first five numbers and three spaces before the sixth. The program ends with a farewell message to the user.

import random

print("Welcome to the PowerBall Lottery Number Generator!")

# Generate five random numbers for the white balls (1-69)
white_ball1 = random.randint(1, 69)
white_ball2 = random.randint(1, 69)
white_ball3 = random.randint(1, 69)
white_ball4 = random.randint(1, 69)
white_ball5 = random.randint(1, 69)

# Generate one random number for the red PowerBall (1-26)
power_ball = random.randint(1, 26)

# Print the numbers with the specified spacing
print(f"Your lottery numbers are: {white_ball1} {white_ball2} {white_ball3} {white_ball4} {white_ball5}   {power_ball}")

print("Good luck, and thanks for playing!")
