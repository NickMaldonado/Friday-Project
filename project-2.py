import random

def generate_powerball_numbers():
    print("Welcome to the PowerBall number generator!")
    response = input("Would you like some PowerBall numbers? (yes/no): ")

    if response.lower() == "yes":
        # Generate the first five white ball numbers
        white_ball1 = random.randint(1, 69)
        white_ball2 = random.randint(1, 69)
        white_ball3 = random.randint(1, 69)
        white_ball4 = random.randint(1, 69)
        white_ball5 = random.randint(1, 69)

        # Generate the red ball number
        red_ball = random.randint(1, 26)

        # Print the generated numbers with proper spacing
        print("Your PowerBall numbers are: {}  {}  {}  {}  {}    {}  ".format(white_ball1, white_ball2, white_ball3, white_ball4, white_ball5, red_ball))
    else:
        print("No problem! Come back when you're ready to play!")

    print("Thank you for using the PowerBall number generator. Goodbye!")

if __name__ == "__main__":
    generate_powerball_numbers()
