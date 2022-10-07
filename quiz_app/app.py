# Create dict with keys and values for the answers
quiz = {
    "What is the capital of France?": "Paris",
    "What is the capital of Germany?": "Berlin",
    "What is the capital of Spain?": "Madrid",
    "What is the capital of Italy?": "Rome",
    "What is the capital of Poland?": "Warsaw",
}

SCORE = 0

# Loop through the quiz dict
for question, answer in quiz.items():
    # Ask the question
    print(question)
    # Get the user's answer
    user_answer = input("Your answer: ")
    # Check if the answer is correct
    if user_answer.capitalize() == answer.capitalize():
        # Print a message
        print("Correct!")
        # Add one to the score
        SCORE += 1
    else:
        # Print a message
        print("Wrong!")

# Print the final score
print(f"Your final score is: {SCORE} / {len(quiz)}")
