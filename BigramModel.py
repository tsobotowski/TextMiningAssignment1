import os
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter, defaultdict
import math

freq_by_genre = {}
validation_set = {}

nltk.download('punkt')

def read_files_in_directory(directory_path):
    dic_term_frequency = Counter()
    dic_pairs_frequency = Counter()

    
    for file in os.listdir(directory_path):
        with open(os.path.join(directory_path, file), 'r') as rfile:
            for line in rfile:
                current_line = line.strip().lower()
                tokens = word_tokenize(current_line)
                
                dic_term_frequency.update(tokens)
                
                if len(tokens) > 1:
                    bigrams = zip(tokens[:-1], tokens[1:])
                    dic_pairs_frequency.update(bigrams)

    return dic_term_frequency, dic_pairs_frequency

def process_song(path): #processes an individual song
    with open(path, 'r') as rfile:
        dic_term_frequency = Counter()
        dic_pairs_frequency = Counter()
        for line in rfile:
            current_line = line.strip().lower()
            tokens = word_tokenize(current_line) 
            dic_term_frequency.update(tokens)
                
        if len(tokens) > 1:
            bigrams = zip(tokens[:-1], tokens[1:])
            dic_pairs_frequency.update(bigrams)

def freq_to_prob(dic_term_frequency, dic_pairs_frequency):
    dic_term_prob = defaultdict(dict)
    
    for (w1, w2), pair_count in dic_pairs_frequency.items():
        dic_term_prob[w1][w2] = pair_count / dic_term_frequency[w1]

    return dic_term_prob

def calculate_probability(dic_term_prob, input_text):
    tokens = word_tokenize(input_text.lower())
    prob = 0.0
    
    for i in range(len(tokens) - 1):
        w1, w2 = tokens[i], tokens[i + 1]
        if w1 in dic_term_prob and w2 in dic_term_prob[w1]:
            prob += math.log(dic_term_prob[w1][w2], 2)
        else:
            prob += math.log(1e-6, 2)  # Smoothing for unseen bigrams

    return prob

def prob_by_genre(genre, text, freq_by_genre):
    dic_term_frequency, dic_pairs_frequency = freq_by_genre[genre]
    dic_term_prob = freq_to_prob(dic_term_frequency, dic_pairs_frequency)
    prob = calculate_probability(dic_term_prob, text)
    return prob

def predict(text):
    probByGenre = {}
    for genre in freq_by_genre:
        probByGenre[genre] = prob_by_genre(genre, text, freq_by_genre)
    return probByGenre


