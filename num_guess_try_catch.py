#!/usr/bin/envpython3
# Created By:Deepak
# Date: 11/02/2026
# This program is based on guessing a random number to see if you get it right or not
import random


def main():

    generated_num = random.randint(0, 9)
    num_guess_as_string = input("Please guess a number between 0-9: ")

    # the try statement will try the use input and see if its valid or not
    try:

        num_guess_as_num = int(num_guess_as_string)

        # the if statement will see if the input is the same has the generated num
        if num_guess_as_num == generated_num:

            print("You guessed correctly!")
        # the else statement operates if the if statement doesn't
        else:
            print(
                "Your guess was incorrect, the correct answer was: {}".format(
                    generated_num
                )
            )
    # the except statement is if the input wasn't valid
    except:

        print(
            "({})Is not a valid value. (MUST BE A NUMBER)".format(num_guess_as_string)
        )

    # finally statement for the outro of the program
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
