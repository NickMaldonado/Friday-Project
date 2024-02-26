# Friday-Project

# Mad Lib Game Python Script

## Code Explanation:

1. `def mad_lib():` - Defines a function named `mad_lib` to encapsulate the Mad Lib game logic.

2. `print("Welcome to the Mad Lib game!")` - Prints a welcome message to the player.

3. `print("Please provide the following words:")` - Prompts the player to provide words for the Mad Lib story.

4. `large_object = input("A large object: ")` - Asks the player to input a large object and stores it in the variable `large_object`.

5. `large_objects_plural = input("Large objects (plural): ")` - Asks the player to input plural large objects and stores them in the variable `large_objects_plural`.

6. `adjective = input("An adjective: ")` - Asks the player to input an adjective and stores it in the variable `adjective`.

7. `body_part = input("A body part: ")` - Asks the player to input a body part and stores it in the variable `body_part`.

8. `restaurant = input("A restaurant: ")` - Asks the player to input a restaurant and stores it in the variable `restaurant`.

9. `first_food = input("A food: ")` - Asks the player to input a food and stores it in the variable `first_food`.

10. `second_food = input("Another food: ")` - Asks the player to input another food and stores it in the variable `second_food`.

11. `print("\nHere's your Mad Lib story:\n")` - Prints a message indicating that the Mad Lib story is about to be displayed.

12. `print("I’ve had a very", adjective, "day.")` - Prints the first line of the Mad Lib story with the adjective provided by the player.

13. `print("This morning, I dropped a box of", large_objects_plural, "on my", body_part + ".")` - Prints the second line of the Mad Lib story with the plural large objects and body part provided by the player.

14. `print("Then, at lunch, I went to", restaurant, "for their delicious", first_food + ",")` - Prints the third line of the Mad Lib story with the restaurant and first food provided by the player.

15. `print("But the waiter brought me", second_food + ", which I was not hungry for.")` - Prints the fourth line of the Mad Lib story with the second food provided by the player.

16. `print("Finally, on my way home, I was cut off by a van with a large", large_object, "strapped to the roof.")` - Prints the final line of the Mad Lib story with the large object provided by the player.

17. `if __name__ == "__main__":` - Checks if the script is being run directly.

18. `mad_lib()` - Calls the `mad_lib()` function if the script is run directly, initiating the Mad Lib game.


# PowerBall Number Generator Python Script

## Code Explanation:

1. `import random` - Imports the `random` module to generate random numbers.

2. `def generate_powerball_numbers():` - Defines a function named `generate_powerball_numbers` to encapsulate the PowerBall number generation logic.

3. `print("Welcome to the PowerBall number generator!")` - Prints a welcome message to the user.

4. `response = input("Would you like some PowerBall numbers? (yes/no): ")` - Prompts the user to input whether they want PowerBall numbers and stores their response in the variable `response`.

5. `if response.lower() == "yes":` - Checks if the user's response is "yes" (case insensitive).

6. `white_ball1 = random.randint(1, 69)` - Generates a random number between 1 and 69 for the first white ball and stores it in the variable `white_ball1`. This process is repeated for the next four white balls and the red ball.

7. `print("Your PowerBall numbers are: {}  {}  {}  {}  {}    {}  ".format(white_ball1, white_ball2, white_ball3, white_ball4, white_ball5, red_ball))` - Prints the generated PowerBall numbers with proper spacing between them.

8. `else:` - Executes if the user's response is not "yes".

9. `print("No problem! Come back when you're ready to play!")` - Prints a message indicating the user chose not to generate PowerBall numbers.

10. `print("Thank you for using the PowerBall number generator. Goodbye!")` - Prints a farewell message to the user.

11. `if __name__ == "__main__":` - Checks if the script is being run directly.

12. `generate_powerball_numbers()` - Calls the `generate_powerball_numbers()` function if the script is run directly, initiating the PowerBall number generation process.

# Trivia Question Study Program Python Script

## Code Explanation:

1. `def study_questions(questions):` - Defines a function named `study_questions` that takes a dictionary of questions and answers as input.

2. `print("Welcome to the trivia question study program!")` - Prints a welcome message to the user.

3. `for question, answer in questions.items():` - Iterates through each question-answer pair in the dictionary.

4. `print("\nQuestion:", question)` - Prints the current question to the user.

5. `user_answer = input("Your answer: ")` - Prompts the user to input their answer to the current question and stores it in the variable `user_answer`.

6. `if user_answer.lower() == answer.lower():` - Checks if the user's answer (converted to lowercase) matches the correct answer (also converted to lowercase).

7. `print("Correct!")` - Prints a message indicating that the user's answer is correct.

8. `else:` - Executes if the user's answer is incorrect.

9. `print("Incorrect. The correct answer is:", answer)` - Prints a message indicating that the user's answer is incorrect and displays the correct answer.

10. `if __name__ == "__main__":` - Checks if the script is being run directly.

11. `trivia_questions = { ... }` - Defines a dictionary `trivia_questions` containing trivia questions as keys and their corresponding answers as values.

12. `study_questions(trivia_questions)` - Calls the `study_questions` function with the `trivia_questions` dictionary as input, initiating the trivia question study process.

