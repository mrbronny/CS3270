textfile = input("Enter the name of text file: ")
print(f"Statistics for file {textfile}:")
with open(textfile, "r") as file:
  file = file.read()
  characters = 0
  uppers = 0
  lowers = 0
  digits = 0
  whitespace = 0
  vowels = {"a":0,"e":0,"i":0,"o":0,"u":0}
  consonants = 0
  words = 0
  wordsPerSent = []
  for char in file:
    if char.isupper():
      uppers += 1
    if char.islower():
      lowers += 1
    if char.isdigit():
      digits += 1
    elif char in [" ","\n"]:
      whitespace += 1
      words += 1
    elif char.lower() in vowels:
      vowels[char.lower()] += 1
    elif char.isalpha():
      consonants += 1
    elif char in [".","!","?"]:
      wordsPerSent += [words]
      words = 0
    characters += 1
  print(f"Characters: {characters}")
  print(f"Upper case: {uppers}")
  print(f"Lower case: {lowers}")
  print(f"Digits: {digits}")
  print(f"Whitespace: {whitespace}")
  print(f"Vowels: {vowels}")
  print(f"Consonants: {consonants}")
  print(f"Sentences: {len(wordsPerSent)}")
  print(f"Average words per sentence: {sum(wordsPerSent)/len(wordsPerSent)}")