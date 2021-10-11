# # 1a. Average value
# # Write a program that prompts the user to enter numbers (float).
# # The program shows the average value of all entered numbers after each entry.
# # PS. 1a can do without a list

input_string = input("Enter a list element separated by space ")
My_list  = input_string.split()
sum = 0
avg=0
for num in My_list:
    sum += int (num)
    avg=sum/len(My_list)
print("Sum = ",sum)
print("Average = ", avg)


# # 1b. The program shows both the average value of the numbers and ALL the numbers entered
# # PS Exit the program  by entering "q"

input_string = input("Enter a list element separated by space ")
My_list  = input_string.split()
sum = 0
avg=0
for num in My_list:
    sum += int (num)
    avg=sum/len(My_list)
print("Sum = ",sum)
print("Average = ", avg)
print(f"You entered these numbers: {input_string}")
exit_code=input("Enter q to exit")
if exit_code == "q":
    exit()


# # 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.
#

list_numbers = []

while True:
    user_input = input("Input a number or 'q' to quit: ")
    if user_input.lower() == 'q':
        print("Thank you! Exiting")
        break
    else:
        list_numbers.append(float(user_input))
        print(f"All numbers: {list_numbers}\nAverage is {sum(list_numbers) / len(list_numbers):.2f}")
        print(f"BOTTOM 3 {sorted(list_numbers)[:3]}")
        print(f"TOP 3 {sorted(list_numbers)[-3:]}")


#
# 2. Cubes
# The user enters the beginning (integer) and end number.
# The output is the entered numbers and their cubes
# For example: inputs 2 and 5 (two inputs)
# Output
# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125
# All cubes: [8,27,64,125]
# PS could theoretically do without a list, but with a list it will be more convenient


first_no=int(input("Enter the first number: "))
second_no=int(input("Enter the second number: "))
no_list=[]
no_list.append(first_no)
no_list.append(second_no)
print(f"You have entered: {no_list}")
cubes=[n**3 for n in no_list]
print(f"All cubes: {cubes}")
for el,i in no_list,cubes:
     print(f"{el} cubed is {i}")


# 3. Reversed words
# The user enters a sentence.
# We output all the words of the sentence in reverse form. - not the whole text reversed!!
# Example
# Alus kauss mans -> Sula ssuak snam
# PS Split and join operations could be useful here.



sentence = input("Your sentence: ")
sentence_list = sentence.split()
print(sentence_list)
reversed_list = [i[::-1] for i in sentence_list]
new_sentence = " ".join(reversed_list)
print(new_sentence)


# 4. Prime numbers -
# this could be a weekend assignment, there is hardly enough time in class
# Find and output the first 20 (even better option to choose how many first primes we want) prime numbers in the form of a list i.e. [2,3,5,7,11, ...]