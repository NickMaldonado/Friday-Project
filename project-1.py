def mad_lib():
    print("Welcome to the Mad Lib game!")
    print("Please provide the following words:")

    large_object = input("A large object: ")
    large_objects_plural = input("Large objects (plural): ")
    adjective = input("An adjective: ")
    body_part = input("A body part: ")
    restaurant = input("A restaurant: ")
    first_food = input("A food: ")
    second_food = input("Another food: ")

    print("\nHere's your Mad Lib story:\n")
    print("I’ve had a very", adjective, "day.")
    print("This morning, I dropped a box of", large_objects_plural, "on my", body_part + ".")
    print("Then, at lunch, I went to", restaurant, "for their delicious", first_food + ",")
    print("But the waiter brought me", second_food + ", which I was not hungry for.")
    print("Finally, on my way home, I was cut off by a van with a large", large_object, "strapped to the roof.")

if __name__ == "__main__":
    mad_lib()

