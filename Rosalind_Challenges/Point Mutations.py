
def hamming_distance(s, t):
    diff = 0
    for tup in zip(s, t):
        if tup[0] != tup[1]:
            diff += 1
    return diff

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

file = open("data/rosalind_hamm.txt", "r").read()
file = file.split("\n")

print(hamming_distance(file[0], file[1]))