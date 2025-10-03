def print_every_fifth(x):
  while x >= 0:  # x is the loop variable
    print(x)
    x = x - 5
  # when indentation stops, while loop is over
  print("Done!")

def square_user_nums():
  # Initialize loop variable
  user_inp = input("Enter the next number (negative to quit): ") # Does not run because user_num needs to be defined.
  user_num = int(user_inp)
  while user_num >= 0:
    print(user_num, "squared is", user_num ** 2)
    user_inp = input("Enter the next number (negative to quit): ")
    user_num = int(user_inp) # Runs infinite amount of times without stopping.


def sum_to_n(topNum):
    """
    Takes in a number and computes and returns the sum of the numbers
    from zero to the input number.
    """
    curr_val = 0  # the loop variable
    total = 0  # the accumulator variable
    while curr_val < topNum:
        total = total + curr_val  # add next value to accumulator
        curr_val = curr_val + 1  # update the loop variable

    return total

def add_user_nums():
    



