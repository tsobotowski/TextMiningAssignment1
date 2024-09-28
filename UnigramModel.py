import math
import os
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

freq_by_genre = {}

# might be useful?
from collections import Counter


def read_files_in_directory(directory_path):
    # key: tokens value: their frequency in all songs belonging to a genre
    dic_term_frequency = {}
    for file in os.listdir(directory_path):
        with open(directory_path + file, 'r') as rfile:
            for line in rfile:
                current_line = line.strip()
                # pre-process each line if you want to and save the results in current_line
                # YOUR CODE

                tokens = word_tokenize(current_line)
                for token in tokens:
                    if token not in dic_term_frequency:
                        dic_term_frequency[str(token)] = 1
                    else:
                        dic_term_frequency[str(token)] = (dic_term_frequency[str(token)] + 1)

    return dic_term_frequency


def freq_to_prob(dic_term_frequency):
    dic_term_prob = {}
    total_tokens = 0
    for value in dic_term_frequency.values():
        total_tokens += value
    for key in dic_term_frequency.keys():
        dic_term_prob[key] = dic_term_frequency[key] / total_tokens

    return dic_term_prob


def calculate_probability(dic_term_prob, input_text):
    tokens_in = word_tokenize(input_text)
    prob = 0.0
    for token in tokens_in:
        if token in dic_term_prob:
            prob += dic_term_prob[token]
    prob = math.log(prob, 2)
    return prob

def prob_by_genre(genre, text, freq_by_genre):
    prob = calculate_probability(freq_to_prob(freq_by_genre[genre]), text) 
    return prob

def predict(text):
    probByGenre = {}
    for genre in freq_by_genre:
        probByGenre[genre] = prob_by_genre(genre, text, freq_by_genre)
    return probByGenre

path = 'C:/Users/Thad/Documents/COS470/TM_CA1_Lyrics'
for genre in os.listdir(path):
    read_files_in_directory(path + '/' + genre + '/')




