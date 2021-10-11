def calc(a,b=5,c=10):

    return a+b+c

print(calc(5) + calc(10,20) + calc(1,2,3))

# 1. The Big Result
#
# Write an add_mult function that requires three parameters / arguments
#
# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.
#
# PS Assume that numeric parameters will always be passed to the function, no need to check types
#
# Various solutions are possible (you are allowed to use other data structures inside function such as list).
#
# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30



def add_mult(*my_nums):
    my_nums = [int(t) for t in input("Enter three values separated by whitespace: ").split(" ")]
    my_nums.sort()
    result = (my_nums[0]+my_nums[1]) * my_nums[-1]
    return result

print(add_mult())





#
# 2. Palindrome
#
# Write the function is_palindrome (text)
#
# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.
#
# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.
#
#
#
# is_palindrome ("Alus ari i ra    sula") -> True
#
# is_palindrome("ABa") -> True
#
# is_palindrome("nava") -> False
#



def is_palindrome(input_text):
    input_text = input_text.replace(" ", "").lower()
    reversed_text = input_text[::-1]
    return input_text == reversed_text















# 3. City Population
#
#
#
# The city has a known population p0
#
# A percentage of population perc is added each year
#
# Every year a certain number of delta also arrive (or leave)
#
# We need to know when (if at all) the city will reach a population of p
#
# Write a function get_city_year (p0, perc, delta, p) that returns the years (full) when p is reached.
#
# If p cannot be reached, then we return -1
