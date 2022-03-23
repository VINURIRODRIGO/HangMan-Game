#HangMan Game
import random
import HangManGameWordList as wordList
import HangManGameImages as images
randomWord = wordList.list()[random.randint(0,(len(wordList.list())-1))]
HangManGameArt = images.images()
guessWord = []
count= 1
for i in randomWord:
    guessWord.append ("_ ")
print(HangManGameArt[0])
print("Pssst, the solution is lucky.")
print(randomWord)
while count<=6:
    guessLetter = input("\nGuess a letter: ")
    if(randomWord.find(guessLetter)==-1):
        print(f"You guessed {guessLetter}, that's not in the word. You lose a life.")
        count+=1
    elif (count!=7):
        for i in range(len(randomWord)):
          if(randomWord[i]==guessLetter):
              guessWord[i]=" "+guessLetter+" " 
          if(guessWord[i]=="_ "):
              guessWord[i]="_ "  
    if(count==7):
        print("You lose")
    elif(" "+guessLetter+" " in guessWord):
              print(f"You've already guessed {guessLetter}")    
    for i in guessWord:          
        print(i,end="")
    if(guessWord.count("_ ")==0):
        print("\nYou win")
        print(HangManGameArt[count])
        break
    print("\n\n"+HangManGameArt[count])
