import itertools
from spellchecker import SpellChecker
spell = SpellChecker()
unscrambledwords = {}

min_len = input("Minimum length of anagrams: ")
while min_len.isnumeric() == False:
    input("You must input an integer. Minimum length of anagrams: ")
min_len = int(min_len)



with open("wordstounscramble.txt","r") as file:
    data = file.read()
unscrambledlist = data.split("\n")
for word in unscrambledlist:
    unscrambledwords[word] = []
    for i in range(min_len,len(word)+1):
        for comb in itertools.permutations(word,i):
            comb = "".join(n for n in comb)
            if len(spell.known([comb])) != 0:
                    unscrambledwords[word].append(comb)

f = open("wordsunscrambled.txt","w")
for i in unscrambledwords:
    print(f"{i}: {unscrambledwords[i]} \n")
    f.write(f"{i}: {unscrambledwords[i]} \n")



