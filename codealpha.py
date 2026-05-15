import random

def hangman():
    words = ["python", "java", "laptop", "intern", "github"]
    word = random.choice(words)
    word_letters = list(word) # ['p','y','t','h','o','n']
    guessed = ["_"] * len(word) # ['_','_','_','_']
    guessed_letters = []
    tries = 6

    print("=== HANGMAN GAME ===")
    print("Word:", " ".join(guessed))
    print(f"Tumhare paas {tries} galat guesses hai\n")

    while tries > 0 and "_" in guessed:
        guess = input("Ek letter guess karo: ").lower()

        if len(guess)!= 1 or not guess.isalpha():
            print("Sirf 1 letter daalo bhai!\n")
            continue

        if guess in guessed_letters:
            print("Ye letter pehle try kar chuki ho!\n")
            continue

        guessed_letters.append(guess)
        if guess in word_letters:
            print("Sahi hai!\n")
            # Saari jagah update karo
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            tries -= 1
            print(f"Galat! {tries} tries bache hai\n")

        print("Word:", " ".join(guessed))
        print("Guessed letters:", ", ".join(guessed_letters))
        print("-" * 30)

    if "_" not in guessed:
        print(f"\nJeet gayi! Word tha: {word}")
    else:
        print(f"\nHaar gayi Word tha: {word}")
hangman()