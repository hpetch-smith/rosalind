# given a nucleotide sequence return A C G T counts as a string of numbers in same order 
# count nucleotides
def count_nucleotides(seq):
    # nuceleotides to count
    nucleotides = ['A','C','G','T']
    # array to store counts 
    counts = []
    # loop through nucleotides 
    for base in nucleotides:
        # count 
        counts.append(seq.count(base))
    # convert to string    
    counts = map(str,counts)
    # return in string format
    return ' '.join(counts)


if __name__ == '__main__':
    # get filename
    filename = 'Data/rosalind_dna.txt'
    # open file 
    with open(filename) as seq:
        # read content
        seq = seq.read()
    
    print(count_nucleotides(seq))