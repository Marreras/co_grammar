# Example 1

poke_list = ["Picachu", "Charizar", "Gengar", "Squirtle"]

print(poke_list)
print("This is the list")

for i in poke_list:
    print("Current Pokemon: ", i)
    print("This is the list!")

    # "i" is temporary variable, and we could use any "name", no just "i" 

for poke in poke_list:
    print("Current Pokemon: ", poke)

# Example 2

random_sentence = "Hello there General Kenoby"

for letter in random_sentence:
    print(letter)


# Example 3
# range  (6) = [1, 2, 3, 4, 5]
#               0  1  2  3  4   - true list as read in memory

for number in range(1, 6):
    print(number)  

for number in range(0, 10, 2):
    print(number)

# Example 4

for i in range(1, 5):
    print("outer Loop position", i)
    for j in range(1, 5):
        print("inner Loop position", j)
        print(i*j)
    print()


# There is a GPT search about end=" " The end=" " is setting the end parameter of the print() function to a space character " ". This means that instead of printing a newline character at the end of each inner loop iteration, a space character will be printed, causing the next value to be printed on the same line separated by a space., 
# And the print()  is used to print a newline character. This ensures that after each inner loop completes its execution (after printing the inner loop values separated by spaces), a newline character is printed.


for i in range(1, 5):
    print("outer Loop position", i)
    for j in range(1, 5):
        print("inner Loop position", j)
        print(i*j, end=" ")
    print()

# Example 5

random_sent = "Well, of course I know him, he is me"
random_sent_split = random_sent.split(" ")
print(random_sent_split)

for letter in random_sent_split:
    print(letter)