n = int(input())
words = []
count = []
distinctWords = []  # Distinct word is SET of words
for i in range(n):
    words.append(input())

for i in range(len(words)):
    c = 0
    for j in range(len(words)):
        if words[i] == words[j]:    # counting the occurence of words
            c += 1
    if words[i] not in distinctWords:
        distinctWords.append(words[i])
        # typecasted because join is used while converting list to str
        count.append(str(c))

print(len(distinctWords))
print(' '.join(count))
