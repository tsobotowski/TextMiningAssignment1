# MixedModel

Combines unigram and bigram language models to predict the genre of a song

#Usage

Lyrics in the form of text files must be in folders labeled with the appropriate genre. The genre must be in the project source folder and the path copied to 'directory_path' in the mixed_model file. Call the optimize function on a string of text.

The output is the predicted genre for 10 values of lambda, an integer between zero and one that controls how much the predictions of each model affect the final prediction.