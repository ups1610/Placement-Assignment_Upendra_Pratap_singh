# Write a program to count the number of verbs, nouns, pronouns, and adjectives in a given particular phrase or
# paragraph, and return their respective count as a dictionary.

# Example-1 Subject verb object is one of six main word orders across all languages.
# Output-1 {'nouns': 5, 'pronouns': 0, 'verbs': 1, 'adjectives': 2}
# Explanation: In this sentence is->verb , main and across -> adjectivies and Subject,verb,object,six,word ->nouns


# Example -2 We watched a scary movie.
# Output-2 {'nouns': 1, 'pronouns': 1, 'verbs': 1, 'adjectives': 1}
# Explanation: In this sentence We->pronoun , watched->verb , scary->adjective and movie->noun


import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')

def count_from_phrase(string):
    # Tokenize the text into individual words
    words = word_tokenize(string)
    
    # Perform Part-of-Speech (POS) tagging on the words
    tagged_words = pos_tag(words)
    
    # Initialize count variables
    verb = 0
    noun = 0
    pronoun = 0
    adjective = 0
    
    # Iterate over the tagged words and count the POS tags
    for word, tag in tagged_words:
        if tag.startswith('VB'):  # Verb tags start with 'VB'
            verb += 1
        elif tag.startswith('NN'):  # Noun tags start with 'NN'
            noun += 1
        elif tag.startswith('PRP'):  # Pronoun tags start with 'PRP'
            pronoun += 1
        elif tag.startswith('JJ'):  # Adjective tags start with 'JJ'
            adjective += 1
    
    # dictionary creation
    dic = {
        "nouns": noun,
        "pronouns": pronoun,
        "verbs": verb,
        "adjectives":adjective
    }
    
    return dic

# Example usage
string = input("Enter the string/phrase/paragraph:\n")
counts = count_from_phrase(string)
print(counts)
