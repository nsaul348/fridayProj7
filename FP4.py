# Define a dictionary with questions as keys and correct answers as values
questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the smallest planet in our solar system?": "Mercury",
    "How many continents are there?": "7",
    "What is the boiling point of water in Celsius?": "100"
}

print("Welcome to the Quiz Bowl! Answer the questions to test your knowledge.")

# Loop through each question in the dictionary
for question, correct_answer in questions.items():
    # Display the question and prompt the user for an answer
    user_answer = input(f"{question} ").strip()
    
    # Check if the user's answer is correct
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
    
print("Thank you for playing Quiz Bowl! Happy studying!")