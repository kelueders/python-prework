# Question 1
def hello_name(user_name):
    print("hello_" + user_name)

# Question 2
def first_odds():
    numbers = list(range(0,100))
    for number in numbers:
        if number % 2 == 1:
            print(number)

# Question 3
def max_num_in_list(a_list):
    a_list.sort()
    return a_list.pop()


# Question 4
def is_leap_year(a_year):
    if ((a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0)):
        return True
    return False

# Question 5 - returns True if a list has consective numbers
def is_consecutive(a_list):
    return list(range(min(a_list), max(a_list) + 1)) == sorted(a_list)
        





    
    