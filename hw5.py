# 1. Confusion

name = input("Please enter your name: ")
reverse_name = name[::-1]
text = ",a thorough mess is it not "
print(reverse_name.title() + text + "?")

# 2. Almost Hangman

word = input("First player, enter the text: ")
guess_text = ""
for c in word:
    if c == " ":
        guess_text += " "
    else:
        guess_text += "*"
print(guess_text)

guess = input("Input a letter to guess: ")

guess_text = ""  # to make a full game we would want to preserve the guess so far

for c in word:
    if c == " ":
        guess_text += " "
    elif c == guess:
        guess_text += c
    else:
        guess_text += "*"

print(guess_text)

# 3. Text conversion

sentence=input("Enter your text:")
for word in sentence:
    if "not" and "bad" in sentence:
        print(sentence.replace("not", "").replace("bad", "good"))
        break
    else:
        print(sentence)
        break