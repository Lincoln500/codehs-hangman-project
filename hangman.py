import random


letter = ""
guesses_left = int(10)
words = ["cama", "bota", "sol", "hello"]
secret_word = random.choice(words)
dashes = len(secret_word) * "-"


def get_guess(dashes, guesses_left):
    stop = False
    letter = " "

    if dashes == secret_word:
        stop = True
        print("Congrats! You win.")

    if guesses_left == 0:
        stop = True
        print("You lose")

    while not(letter in secret_word) and not stop:
        #print("entrei no laco " + str(stop))
        print(dashes)
        print(str(guesses_left) + " incorrect guesses left.")
        letter = input("guess: ")
        if not letter.islower() and len(letter) == 1:
            print("Your guess must be a lowercase letter!")
        if len(letter) > 1:
            print("Your guess must have exactly one character!")
        update_dashes(secret_word, dashes, letter, guesses_left)


def update_dashes(secret_word, dashes, letter, guesses_left):
    result = ""
    count = -1
    count_dash = 0
    if letter in secret_word and letter != "":
        print("That letter is in the word!")
        for i in secret_word:
            count = count + 1
            count_dash = count_dash + 1

            if i.find(letter) == 0:
                #dashes = (len(secret_word) - count_dash) * "-"
                dashes = dashes[:count] + secret_word[count] + dashes[count+1:]
    else:
        print("That letter is not in the word!")
        guesses_left = guesses_left - 1
    get_guess(dashes, guesses_left)


get_guess(dashes, guesses_left)
