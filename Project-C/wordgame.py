from random import choice, shuffle

def is_subword(word, subword):
  clist = []
  for c in word:
    clist += [c]
  for c in subword:
    if c in clist:
      clist.pop(clist.index(c))
    else:
      return False
  return True

def notgameover(gamedict):
  for key in gamedict.keys():
    if "-"*key in gamedict[key]:
      return True
  print("YOU WON!!!")
  return False

def shuffleword(word):
  word = list(word)
  shuffle(word)
  return ''.join(word)

def show_answers(answersdict):
  for value in answersdict.values():
    print(value)
  

def main():
  user = input("Enter the range of word lengths (low,high): ")
  user = user.split(",")
  therange = list(range(int(user[0]),int(user[1])+1))
  rangedwords = []
  choices = []
  #grab all words within length parameters from file
  with open("words.txt", "r") as file:
    file = file.readlines()
    for word in file:
      word = word.strip()
      if len(word) in therange:
        rangedwords += [word]
        if len(word) == therange[-1]:
          choices += [word]
  theword = choice(choices)
  answerdict = {}
  gamedict = {}
  for word in rangedwords:
    if is_subword(theword, word):
      if len(word) in answerdict.keys():
        answerdict[len(word)] += [word]
        gamedict[len(word)] += ["-"*len(word)]
      else:
        answerdict[len(word)] = [word]
        gamedict[len(word)] = ["-"*len(word)]
  while notgameover(gamedict):
    gamestring = f"{shuffleword(theword)}:\n\n"
    for value in gamedict.values():
      gamestring += f"{value}\n"
    print(gamestring)
    guess = input("Enter a guess: ")
    verdict = "Sorry. Try again."
    if guess == "q":
      show_answers(answerdict)
      break
    for value in answerdict.values():
      if guess in value:
        if guess in gamedict[len(guess)]:
          verdict = "You already guessed that."
        else:
          verdict = "Correct!"
          index = value.index(guess)
          gamedict[len(guess)][index] = guess
    print(verdict)
    show_answers(answerdict)
  
  
if __name__ == "__main__":
  main()
  