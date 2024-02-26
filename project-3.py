def study_questions(questions):
    print("Welcome to the trivia question study program!")

    for question, answer in questions.items():
        print("\nQuestion:", question)
        user_answer = input("Your answer: ")

        if user_answer.lower() == answer.lower():
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", answer)

if __name__ == "__main__":
    # Define a dictionary with trivia questions and answers
    trivia_questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
        "What is the chemical symbol for water?": "H2O",
        "Which planet is known as the Red Planet?": "Mars",
        "What is the tallest mammal?": "Giraffe"
    }

    # Call the function to study the questions
    study_questions(trivia_questions)
