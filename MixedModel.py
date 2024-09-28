import BigramModel as bg
import UnigramModel as ug
import os

def read_files():
    directory_path = 'C:/Users/Thad/Documents/COS470/TM_CA1_Lyrics/'  
    for genre in os.listdir(directory_path):
        ug.freq_by_genre[genre] = ug.read_files_in_directory(directory_path + genre + '/') #Preprocessing without splitting
        bg.freq_by_genre[genre] = bg.read_files_in_directory(directory_path + genre + '/')
        #split(directory_path, genre)
        
def split(directory_path, genre):
    genre_path = directory_path + genre + '/'
    for song in os.listdir(genre_path):
         bg.process_song(genre_path)
         #ug.read_files_in_directory(genre_path)

def predict(text, l): #returns a dictionary of combined probability by genre
    bg_lib = bg.predict(text)
    ug_lib = ug.predict(text)
    combined = bg_lib #copy over keys, vales will be replaced with combined probabilities
    for genre in bg_lib and ug_lib:
        combined[genre] = (l * bg_lib[genre]) + (1 - l) * ug_lib[genre]
    return combined

def optimize(text):
    l = 0
    while l <= 1:
        print(best_guess(predict(text, l)))
        l += 0.1

def best_guess(prob): #Returns predicted genre
    maximum = max(prob.values())
    prob_values = list(prob.values())
    prob_keys = list(prob.keys())
    guess = prob_keys[prob_values.index(maximum)]
    print(guess)
    return(guess)

read_files()

optimize('You used to call me on my cell phoneLate night when you need my loveCall me on my cell phone')