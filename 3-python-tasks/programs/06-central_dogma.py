# INPUT path to amino acid file 
# RETURN a dictionary 
# Key is a tuple (c0, c1, ... , cn) where ci are codons 
# Value is a pair [name, abbreviation] for the amino acid 
def get_amino_acids(file_path): 
    pass

# INPUT path to DNA file 
# RETURN a list [header, DNA] 
# header is first line in the file 
# DNA is a string of letters from remainder of file 
# no whitespace 
def get_DNA(file_path): 
    pass 

#INPUT FAST file 
#RETURN a string representing the protein 
#using the dictionary 
def translate(DNA_d): 
    pass