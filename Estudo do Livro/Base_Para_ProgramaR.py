word = 'Banana'
count = 0
for i in range(len(word)):
    if word[i] =="a":
        count = count+1
print(count)
index = word.find('a')
print(index)

print('a' in 'Macaco')
print('seed' in "macarena" )

print()
print()

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)
x = in_both("macacacco",'macacc')
