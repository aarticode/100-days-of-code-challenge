#Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

import random

# Define questions and their corresponding answers
questions = [
    ("What is the capital of France?", "Paris"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
    ("What is the powerhouse of the cell?", "Mitochondria"),
    ("Which country won the FIFA World Cup in 2018?", "France")
]

def main():
    total_prize = 0
    for question, answer in questions:
        print(question)
        user_answer = input("Your answer: ").strip().capitalize()
        if user_answer == answer:
            print("Correct answer!")
            total_prize += 10000  # Add prize money for correct answer
        else:
            print("Wrong answer! The correct answer is", answer)
            break  # End the game if the answer is wrong
    print("\nCongratulations! You won ${}!".format(total_prize))

if __name__ == "__main__":
    main()

