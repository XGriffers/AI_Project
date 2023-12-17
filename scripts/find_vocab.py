import json
from keras.preprocessing.text import Tokenizer

# Specify the path to your JSON file
file_path = '../data/data.json'

# Load the JSON data
with open(file_path) as f:
    data = json.load(f)

# Extract the text data
text_data = [item['P tags'] for item in data]

# Flatten the list of lists
text_data = [item for sublist in text_data for item in sublist]

# Initialize the tokenizer
tokenizer = Tokenizer()

# Fit the tokenizer on the text data
tokenizer.fit_on_texts(text_data)

# Tokenize the text data
tokens = tokenizer.texts_to_sequences(text_data)

# Flatten the list of lists
tokens = [item for sublist in tokens for item in sublist]

# Calculate the vocabulary size (number of unique tokens)
vocab_size = len(tokenizer.word_index) + 1

# Calculate the maximum sequence length
max_length = max(len(text) for text in text_data)

#print('Tokens',tokens)
print('Vocabulary size:', vocab_size)
print('Max sequence length:', max_length)