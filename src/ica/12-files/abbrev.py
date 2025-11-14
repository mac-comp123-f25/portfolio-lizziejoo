def print_abbrev(file):
    f = open("../TextFiles/alice.txt", 'r')
    for l in f:
        print(l[:20])
    f.close()

print_abbrev("../TextFiles/alice.txt")


