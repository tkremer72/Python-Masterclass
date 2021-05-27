# Create variables to hold the lowest and highest values
low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start:")  # use input to get the computer to wait for the user to hit enter to start the game

# Create a variable to store & count the number of guesses
guesses = 1

while low != high:
    #  print("\tGuessing in the range of {} to {}".format(low, high))

    guess = low + (high - low) // 2  # formula to calculate to mid point between the high and low values

    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h for higher, l for lower, or c if my guess was correct. "
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes 1 less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l, or c")
    # guesses = guesses + 1  # increment the guesses by 1 after each iteration
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses.".format(guesses))