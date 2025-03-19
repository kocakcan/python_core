"""
    - Coupling consists of isolation and mutable arguments.
    - Isolation: The function should be independent of outside things.
      Arguments and return statements are used for external dependencies to a
      small number of well-known places in your code.
    - Mutable arguments: Don't change mutable arguments unless the main idea of
      the function is to change it. Functions that change passed objects create
      lots of coupling.
    - Cohesion refers to the function serving only a single purpose.
    - Single purpose: Each function should do one thing that can be described
      in a simple sentence. Suppose that sentence is comprehensive ("the
      function implements the whole program") or contains lots of conjunctions
      (e.g., "this function does one thing and one more"). Then, you better
      think about splitting it into seperate and simpler functions. Otherwise,
      it might not be easy to re-use it.
    - The function should be relatively small. If your functions start spanning
      multiple pages or have several hundred code lines, it's probably time to
      split them.
"""

# TLDR; The function should be independent of outside things.
# Each function should do one thing and should be relatively small.

# Provide a function to calculate an area for some shapes: square, rectangle,
# or circle.

# Step 1. Defining the Task
# According to the task, the user will provide a type of shape and necessary
# arguments.
# Formulas and required input arguments:
# Shape: square, Square formula: S = a ** 2, Input arguments: a - side length
# of a square
# Shape: rectangle, Square formula: S = a * b, Input arguments: a, b - sides
# length of a rectangle
# Shape: circle, Square formula: S = pi * r ** 2, Input arguments: r - a circle
# radius

# The program will use an input() built-in function to read user data from the
# prompt. Also, there should be a check that the provided shape type is one of
# the predefined values - square, rectangle, or circle. Otherwise, it should
# show a warning message.

def main():
    # Step 2. Initial Code
    # The first variant of code could be the following:
    # shape_type = input("Please, provide a shape you want to calculate area: ")
    #
    # if shape_type == "square":
    #     a = input("side length: ")
    #     if a.isdigit():
    #         a = int(a)
    #         s = a ** 2
    #         print(f"square area: {s}")
    #     else:
    #         print(f"{a} is not a number ")
    #
    # elif shape_type == "rectangle":
    #     a = input("length: ")
    #     b = input("width: ")
    #     if a.isdigit():
    #         a = int(a)
    #         if b.isdigit():
    #             b = int(b)
    #             s = a * b
    #             print(f"rectangle area: {s}")
    #         else:
    #             print(f"{b} is not a number ")
    #
    # elif shape_type == "circle":
    #     r = input("radius: ")
    #     if r.isdigit():
    #         r = int(r)
    #         s = 3.14 * r ** 2
    #         print(f"circle area: {s}")
    #     else:
    #         print(f"{r} is not a number")
    # else:
    #     print(f"I don't know {shape_type} shape ¯\_(ツ)_/¯")

    # Step.3 Isolating a Parameter Request From the User
    # Looking closer at the code, you can see some code duplication. You can
    # get a parameter from the user and check its value. To fix it, you can rewrite
    # the code:
    # def get_user_param(prompt_text=""):
    #     """Get parameter from the user."""
    #     value = input(prompt_text)
    #     if value.isdigit():
    #         return int(value)
    #     else:
    #         print(f"{value} is not a number")
    #
    # shape_type = input("Please, provide a shape for calculate square: ")
    #
    # if shape_type == "square":
    #     a = get_user_param("side length: ")
    #     s = a ** 2
    #     print(f"square area: {s}")
    # elif shape_type == "rectangle":
    #     a = get_user_param("length: ")
    #     b = get_user_param("width: ")
    #     s = a * b
    #     print(f"rectangle area: {s}")
    # elif shape_type == "circle":
    #     r = get_user_param("radius: ")
    #     s = 3.14 * r ** 2
    #     print(f"circle area: {s}")
    # else:
    #     print(f"I don't know {shape_type} mate!")

    # The parameter request was isolated from the user into a seperate method.
    # It enabled the code to be shortened and more readable.

    # Step 4. Moving the Calculation of an Area into Different Methods
    # You can move the calculation of an area of shape into different methods.
    # It might be helpful if you need to re-use a calculation somewhere in
    # other places in the code.
    def get_user_param(prompt_text=""):
        """Get parameter from user."""
        value = input(prompt_text)
        if value.isdigit():
            return int(value)
        else:
            print(f"{value} is not a number")

    def square_area(side_length):
        """Calculate area for square."""
        return side_length ** 2

    def rectangle_area(length, width):
        """Calculate area for rectangle."""
        return length * width

    def circle_area(radius):
        """Calculate area for circle."""
        return 3.14 * radius ** 2

    shape_type = input("Please, provide a shape you want to calculate area: ")

    # if shape_type == "square":
    #     a = get_user_param("side length: ")
    #     print(f"square_area: {square_area(a)}")
    # elif shape_type == "rectangle":
    #     a = get_user_param("length: ")
    #     b = get_user_param("width: ")
    #     print(f"rectangle_area: {rectangle_area(a, b)}")
    # elif shape_type == "circle":
    #     r = get_user_param("radius: ")
    #     print(f"circle_area: {circle_area(r)}")
    # else:
    #     print(f"I don't know {shape_type} matey!")

    def shape_handler(shape_type: str):
        match shape_type:
            case "square":
                a = get_user_param("Side length: ")
                print(f"Square area: {square_area(a)}")
            case "rectangle":
                a = get_user_param("Length: ")
                b = get_user_param("Width: ")
                print(f"Rectangle area: {rectangle_area(a, b)}")
            case "circle":
                r = get_user_param("Radius: ")
                print(f"Circle area: {circle_area(r)}")
            case _:
                print("I don't know what {shape_type} is mate!")


    shape_handler(shape_type)


if __name__ == "__main__":
    main()
