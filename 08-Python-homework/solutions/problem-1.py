import numpy as np
"""
Problem 1
"""

def unique_words(xstring):
    """Problem 1. Find the unique words in a string
        Args: String of text
        Returns: list of unique words in the input text
    """
    # The text might contain both upper case and lower case, so doing simple cleaning to ensure 
    # input contain same case letters and words only.
    input_text = xstring.lower().split()
    word_list = [word.strip('.,!;()[]') for word in input_text] # Removing punctuation.
    unique_word_list = []
    for word in word_list:
        if word not in unique_word_list:
            unique_word_list.append(word)
        else:
            continue
    # Converting set int]o list and return it.
    return unique_word_list


def get_transition_matrix(xtr):
    """Problem 1. Generate the transition matrix
    Args: String of text
    Returns: list of lists which contain transition matrix
    """
    # Getting unique value for the matrix
    unique_words_list = unique_words(xtr)

    # convert unique value list into dict for lookup
    unique_words_dict = {k: v for v, k in enumerate(unique_words_list)}

    # Word list
    input_text = xtr.lower().split()
    word_list = [word.strip('.,!;()[]') for word in input_text]

    # Initialize matrix
    result_matrix = [ [ 0 for i in range(len(unique_words_list)) ] for j in range(len(unique_words_list)) ] 

    for i in range(len(word_list)-1):
        row_value = unique_words_dict[word_list[i]] # Get row index of the word
        col_value = unique_words_dict[word_list[i+1]] # Get column index of next word
        result_matrix[row_value][col_value] += 1 # Update result matrix
    
    return result_matrix


if __name__ == "__main__":

    text = '''The cat is in the house. The dog is outside playing with the kids.
              Both the dog and the cat need a bath. The kids need to come in and eat dinner.'''
    
    uniwords = unique_words(text)
    print(uniwords)
    print(f"There are {len(uniwords)} unique words in the text.")
    print("The transition matrix is below:")
    print(get_transition_matrix(text))