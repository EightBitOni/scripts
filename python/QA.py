# Define a list to store the questions and answers
question_answers = []

# Function to prompt the user for a question and answer
def prompt_question():
    question = input("Enter a question: ")
    answer = input("Enter the answer: ")
    question_answers.append((question, answer))

# Prompt the user for questions and answers
while True:
    choice = input("Do you want to add a question? (y/n): ")
    if choice.lower() == 'y':
        prompt_question()
    else:
        break

# Display the questions and answers
print("\nQuestions and Answers:")
for index, (question, answer) in enumerate(question_answers, start=1):
    print(f"Question {index}: {question}")
    print(f"Answer {index}: {answer}")
    print()
