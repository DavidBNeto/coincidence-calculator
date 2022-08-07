import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a file to be analyzed.")
        exit()
    file = open(sys.argv[1], 'r')
    openedFile = file.readlines()
    lines = ""
    for line in openedFile:
        if len(line) > 1:
            lines = lines + line
    charList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    size = len(lines)
    frequency = 0
    indexOfCoincidence = 0
    for char in charList:
        amount = lines.count(char)
        frequency = (amount / size)
        print(char + ": " + str(frequency))
        indexOfCoincidence = indexOfCoincidence + (frequency ** 2)
    print(str(indexOfCoincidence) + "|" + str(indexOfCoincidence * 26))

