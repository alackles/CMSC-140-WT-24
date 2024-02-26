wordbank = []

with open(r"/home/acacia/Documents/cmsc140/wordle.txt") as f:
    # "Pythonic"
    wordbank = [word.strip() for word in f.readlines()]
    # Typical way
    #for word in f.readlines():
    #    stripword = word.strip()
    #    wordbank.append(stripword)

print(wordbank)

example = "hello"
print(list(example))
print(example[1])