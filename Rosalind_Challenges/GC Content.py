from Bio import SeqIO

def highest_GC(file):

    recs = SeqIO.to_dict(SeqIO.parse(file, 'fasta'))

    gc_ratio = 0

    for record in recs.values():
        id = record.id
        seq = record.seq
        temp_ratio = (seq.count("C") + seq.count("G")) / len(seq) * 100
        if temp_ratio > gc_ratio:
            gc_ratio = round(temp_ratio, 6)
            res = (id, gc_ratio)

    return res

file = open("data/rosalind_gc.txt")
print(highest_GC(file))


