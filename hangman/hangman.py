import random

wo = open("words.txt","r")
data = wo.readline()
words = data.split()
word = random.choice(words)

total_chances = 5
flag = 0

guessed_word = "-" * len(word)
while total_chances != 0:
    print(guessed_word)

    letter = input("Guess a letter: ").upper()

    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1 :]
        if guessed_word == word:
            flag = 1
            print("Congratulations...you won!!!")
            print(word)
            break
    else:
        total_chances -= 1
        print("Incorrect guess")
        print(total_chances, "chances left")
else:
    print("Game Over")
    print()
    print("You lose..all chances are exhausted")
    print()
print("The correct word is:", word)
