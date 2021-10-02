import json

def get_amino_acids(file_path):
    """
        This function will translate input file into dictionary

        -- input
            file_path : amino acid file path
        -- Function
            reading the file using python file handling
            each line we are spliting based on comma 
            and creating dictionary
        -- output
            dict - result as dictonary file
    
    """
    amino_acids = {}
    amino_acids_list = [] 

    file_handle = open(file_path).readlines()
    for line in file_handle:
        s = line.strip().split(", ")
        amino_acids_list.append({"name": s[0],"initial": s[1],"code" : s[2:]})

    amino_acids["data"] = amino_acids_list
        
    return json.dumps(amino_acids)


def get_DNA(file_path):
    """
        This file reads fasta file and split the lines
        -- input
            file_path - fasta file path
        -- output
            list contain name and dna sequence
    """
    dna = open(file_path, "r")
    dna = dna.read().splitlines()
    
    return [dna[0], ''.join(dna[1:])]


def translate(DNA_d):

    """
        This function translate dna into protin based on the amino acid dict
        -- input
            DNA_d - FASTA File
        -- Output
            List of protin list in string format
    """

    amino_acids = json.loads(get_amino_acids("amino_acid.txt"))
    dna = open(DNA_d, "r")
    sequence = dna.read().splitlines()

    protin_list = []
    for i in range(1, len(sequence)):
        char_list = [(sequence[i][j:j+3]) for j in range(0, len(sequence[i]), 3)]
        value=""
        for c in char_list:
            if len(c) == 3:
                for j in amino_acids["data"]:
                    if c in j["code"]:
                        value += j["initial"]
        protin_list.append(value)
    return protin_list