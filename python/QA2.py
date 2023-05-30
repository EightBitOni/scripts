def ask_question(question):
    answer = input(question + " ")
    return answer

# Define the list of questions
questions = [
    "What is your name?",
    "Where are you from?",
    "What is your favorite color?",
    "How old are you?",
    "What is your occupation?"
]

# Create an empty dictionary to store the answers
answers = {}

# Ask the questions and store the answers
for question in questions:
    answer = ask_question(question)
    answers[question] = answer

# Output all the information
print("\nUser Information:")
for question, answer in answers.items():
    print(question + " " + answer)