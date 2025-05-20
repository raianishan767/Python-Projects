import random

words=["samsung","xaomi","symphoney","realme","nokia","vivo","oppo","motorola","moto","redmi","iphone","huawei","nothing","apple","techno","iqoo"]

def chooseWord():
    return random.choice(words)

def playGame():
    word=chooseWord()
    attempt=10
    guessed=["_"]*len(word)
    guessLetter=[]
    print("Guess a mobile company:")

    while attempt>0 and "_" in guessed:
        print(f"Word : {" ".join(guessed)}")
        print(f"Gussed letter : {",".join(guessLetter)}")
        guess=input("Guess a Letter : ").lower()
        print("\n")

        if len(guess)!=1 or not guess.isalpha():
            print("Guess a valid single letter.")
            print("\n")
            continue
        elif guess in guessLetter:
            print("You have already gussed the letter.")
            print("\n")
        
        guessLetter.append(guess)

        if guess in word:
            for i,letter in enumerate(word):
                if letter==guess:
                    guessed[i]=guess
        else:
            attempt-=1
            print(f"You have {attempt} attempts remaining. ")
            
        
    if "_" not in guessed:
        print("You successfully find the word ",word)
    else:
        print("Game Over.The word was ",word)


playGame()