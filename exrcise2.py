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



#Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.
questions = [
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):

    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or  0 to quit:\n"))
    if (reply == 0):
        money = levels[i - 1]
        break
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is {money}")



