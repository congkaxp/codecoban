import random
wordlist = ['apple','banana','orange']
word = random.choice(wordlist)
word1 = list(word)


wordkey = []
l = len(word)
for i in range(0,l):
    wordkey+="_"
wordkey1=" ".join(wordkey)
print('Please guess this word ',wordkey1)
print('Sai quá 3 lần bị out')

k=3
while k>=0:
    guess=input('Guess a letter: ').lower()
    if guess in word:
        for i in range(0,l):
            if word[i]==guess:
                wordkey[i]=guess                          
        wordkey2=" ".join(wordkey)        
        print(wordkey2)
        if '_' not in wordkey2:
            print('well done !')
            break
    else:
        print(f'You have {k} turns')
        k-=1
        if k==-1:
            print('you dead !!! Silly :)))')
    




