with open("poem.txt", mode="r") as readFile:
    allWords = []
    for line in readFile.readlines():
        words = line.strip().split(" ")
        allWords += words
        unique = set(allWords)
        # print(words)
    print(len(unique))
    print(len(allWords))

    with open("unique.txt", mode="w") as writeFile:
        for items in sorted(unique):
            writeFile.write(items)
            writeFile.write("\n")
