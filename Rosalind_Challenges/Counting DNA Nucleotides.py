
def counting_nucleotides(file):

    file = open(file, "r")
    sample = file.read()
    sample = sample.lower()

    adenine = sample.count("a")
    citosine = sample.count("c")
    guanine = sample.count("g")
    timine = sample.count("t")

    return adenine, citosine, guanine, timine

print(counting_nucleotides("data/rosalind_dna.txt"))