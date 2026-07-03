from Bio.SeqUtils import gc_fraction
# Function to calculate GC content and classify each gene
def gc_comparison(input_file , output_file):
    """Calculate GC content of each sequence in a FASTA file."""
    gene=""
    seq=""
    with open(input_file,'r')as f , open(output_file , 'w')as out:
         # Read the FASTA file line by line
        for line in f:
            line=line.strip()
             # Header line indicates the start of a new sequence
            if line.startswith(">"):
                # Process the previous sequence before reading the next one
               if seq:
                   # Calculate GC percentage
                    GC= gc_fraction(seq) *100
                     # Classify based on GC content
                    if GC < 40:
                      classification='LOW GC CONTENT'
                    elif GC<=60:
                      classification='MEDIUM GC CONTENT'
                    else:
                      classification='HIGH GC CONTENT'
                   
                    out.write(f"{gene}\t{GC:.1f}\t{classification}\n") # Write results to the output file

                # Store the new gene name and reset the sequence
               gene=line[1:]
               seq=""

            else :
                seq+=line   # Append DNA sequence lines

        if seq:    # Process the last sequence in the FASTA file
            GC= gc_fraction(seq) *100
            if GC<40:
                classification='LOW GC CONTENT '
            elif GC <=60:
             classification='MEDIUM GC CONTENT'
            else:
              classification='HIGH GC CONTENT'
            out.write(f"{gene}\t{GC:.1f}\t{classification}\n") 
           
# Execute the program
if __name__=="__main__":
    gc_comparison("gene.fa"  ,  "gc_classification.txt")
    print("Classification complete. Results saved to gc_classification.txt")