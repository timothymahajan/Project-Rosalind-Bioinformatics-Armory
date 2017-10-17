#Problem 1: Introduction to the Bioinformatics Armory
#Given: A DNA string s of length at most 1000 bp.
#Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s. Note: You must provide your answer in the format shown in the sample output below.

def CountNucleotides (input, nuc):
    return len(input) - len(input.replace(nuc, ""))

input = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print(str(CountNucleotides(input, "A")) + " " 
      + str(CountNucleotides(input, "C")) + " " 
      + str(CountNucleotides(input, "G")) + " " 
      + str(CountNucleotides(input, "T")))

