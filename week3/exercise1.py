# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""




def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    #count = 0
    #while(count<10):
        #print(count)
        #count = count + 3
    count = start
    count_list = []
    while(count<stop):
        count_list.append(count)
        count = count + step
    return count_list



def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """

    count = 0
    count_list = []
    for count in range(start,stop,step):
        count_list.append(count)
    return(count_list)

        


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    #step = 2
    #for count in range(start,stop,step):
        #print(count)
    count_list = []
    step = 2
    while(start<stop):
        count_list.append(start)
        start = start + step
    return count_list



def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """

    # number = int(input("Please enter a number: "))
    # if 10000 <= number <= 30000:
    #     print("Please enter another number")
    # else:
    #     print("This is a good number")
    while True:
        number = int(input("Enter a number between {} and {}".format(low,high)))
        print(number)
        if low < number < high:
            print("That is a good number")
            return number
        else: 
            print("try again")

    
    


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    # while True:
    #     try:
    #         userInput = int(input(message))
    #         return userInput   
    #     except ValueError:
    #         print("Not an integer! Try again.")
    keep_asking = True
    while keep_asking == True
        Vn = None
        Vstr = input("please enter a number")
        try:
            Vn = float(Vstr)
            keep_asking = False
        except:
            keep_asking = True
    return "correct"

    


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    # while True:
    #     try:
    #         userInput = int(input("Enter a number: ")) 
    #         if low < userInput < high:
    #             print("That is a good number")
    #             return userInput      
    #     except ValueError:
    #         print("Not an integer! Try again.")
    keep_asking = True
    while keep_asking == True
        Vn = None
        Vstr = input("please enter a number between " + str(low) + " and " + str(high) + " :")
        try:
            
        



if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
