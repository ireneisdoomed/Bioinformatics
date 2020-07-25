
def DNA_to_RNA(file):
    file = open(file, "r")
    sample = file.read()
    return sample.replace("T", "U")


print(DNA_to_RNA("data/rosalind_rna.txt"))