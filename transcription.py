# given a sequence of dna transcribe it to rna 
# function to do transcription
def transcribe(seq):
    # replace ts with us 
    return seq.replace('T','U')

if __name__ == '__main__':
    # get sequence file
    filename = 'Data/rosalind_rna.txt'
    # open file
    with open(filename) as seq:
        # read sequence 
        seq = seq.read()
    # print new sequence     
    print(transcribe(seq))