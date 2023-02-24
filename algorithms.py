numbers_list = [35,8,64,46,45,54,123,75,46,35]
best_people_list = ["JJ", "Megan", "Brett", "Dan", "Dan", "Nevin"]

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

#print(one_hundred_check)

# Task 3: Repeated Names

# Will return true if there are any name repeats in the given_list
        # The proper Big O Notation is going to be O(n^2)
def is_multiple_names(given_list):
    name_repeat = False
    index = 0
    count = index + 1

    for name in given_list:
        while count < len(given_list):
            if name == given_list[count]:
                name_repeat = True
                return name_repeat
            count += 1
        index += 1
        count = index + 1

    return name_repeat


does_name_repeat = is_multiple_names(best_people_list)

#print(does_name_repeat)

# Task 4: Sort List

# The Big O Notation is O(n^2)
def bubble_sort(given_list):

    for current_item in range(len(given_list)):
        for compared_item in range(len(given_list) -1, current_item, -1):
            if given_list[compared_item] < given_list[compared_item - 1]:
                temp_number               = given_list[compared_item]
                given_list[compared_item] = given_list[current_item]
                given_list[current_item]  = temp_number
        
print(numbers_list)
bubble_sort(numbers_list)
