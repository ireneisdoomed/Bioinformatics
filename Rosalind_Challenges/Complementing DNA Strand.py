
def reverse_complement(file):

    file = open(file, "r")
    sample = file.read()

    sample = sample[::-1]
    complement = [("A", "T"), ("T", "A"), ("G", "C"), ("C", "G")]

    res = []
    
    for n in sample:
        for tup in complement:
            if n == tup[0]:
                res.append(tup[1])
    
    return "".join(res)



print(reverse_complement("data/rosalind_revc.txt"))