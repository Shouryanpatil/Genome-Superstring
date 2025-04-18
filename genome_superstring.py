from Bio import SeqIO
import itertools

def read_fasta(file_path):
    return [str(record.seq) for record in SeqIO.parse(file_path, "fasta")]

def overlap(a, b, min_length=1):
    """Return length of the maximum suffix of 'a' matching a prefix of 'b'."""
    start = 0 # Start all the way at the left
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

def find_shortest_superstring(reads):
    while len(reads) > 1:
        max_len = -1
        best_pair = (0,0)
        best_merged = ''
        for a, b in itertools.permutations(reads, 2):
            olen = overlap(a, b, min_length=(len(a)//2)+1)
            if olen > max_len:
                max_len = olen
                best_pair = (a, b)
                best_merged = a + b[olen:]
        reads.remove(best_pair[0])
        reads.remove(best_pair[1])
        reads.append(best_merged)
    return reads[0]

# Load reads and solve
reads = read_fasta("input.txt")
result = find_shortest_superstring(reads)
print(result)
