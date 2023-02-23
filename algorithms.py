numbers_list = [35,8,64,46,45,54,123,75,46,35]


# Task 1: Even or Odd

# Will return true if number is even and false if number is odd
def is_even(number):
    return bool(number % 2)

number_1 = is_even(9) 
number_2 = is_even(8)

#print(number_1)
#print(number_2)

        # The proper big O notation would be O(1)

# Task 2: Less than 100

# Will return true if all numbers in given_list are under 100 and false if ANY of the numbers are greater than or equal to 100
        #The proper Big O Notation is going to be O(n)
def is_under_100(given_list):
    under_100 = True

    for number in given_list:
        if number < 100:
            continue
        else:
            under_100 = False
            break

    return under_100

one_hundred_check = is_under_100(numbers_list)

print(one_hundred_check)