import random

listOfWords = open("listOfWords.txt")
wordList = list()
for x in listOfWords:
    wordList.append(x)
wordList = [ x[:5] for x in wordList ]

randomNum = random.randint(1,len(wordList)-1)
guessWord = wordList[randomNum]

print("Игра началась! Попытайся угадать слово из 5 букв.")
GameOver = False
inp = ""
attempt = 5
while not(GameOver):
    if inp == guessWord:
        GameOver = True
        print(f"Угадал! Загаданное слово: {guessWord}")
        break
    
    while True:
        inp = input().upper()
        if not(inp.isnumeric()) and len(inp) == 5:
            break
        else:
            print("\033[41mВВЕДИТЕ СЛОВО ИЗ 5 БУКВ!\033[0m")
    
    for i in range(0,len(inp)-1,1):
        if inp[i] == guessWord[i]:
            print(f'Угадал! Буква \033[32m"{inp[i]}"\033[0m находится в загаданном слове на {i + 1} месте')
        elif inp[i] in guessWord: 
            print(f'Буква \033[33m"{inp[i]}"\033[0m есть в загаданном слове...')
        else: continue

    attempt -= 1
    if attempt != 0: 
        print(f'Попыток осталось: {attempt}...')
    else:
        print(f"Игра проиграна :( Загаданное слово: {guessWord}")
        break
