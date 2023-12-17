import sys
import os
import json
import numpy as np
from model import create_model, prepare_data
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import Callback
from tensorflow.keras.preprocessing.text import Tokenizer

# Set the paths for scripts and data
sys.path.append('../scripts/')
sys.path.append('../data/')

from load_data import load_json, extract_text_data
from process_data import tokenize_text_data

# Load and process the data
file_path = '../data/data.json'
data = load_json(file_path)
text_data = extract_text_data(data)
tokens, tokenizer = tokenize_text_data(text_data)
print('Loading data...')

max_length = 10  # Maximum length of input sequence
max_vocab = 10  # Adjust this value according to your needs

tokenizer = Tokenizer(num_words=max_vocab, oov_token="<OOV>")
tokenizer.fit_on_texts(text_data)
vocab_size = len(tokenizer.word_index) + 1  # Vocabulary size

# Assuming 'tokens' is a list of all tokens in the dataset
sequence_length = 10  # The length of each input sequence
sequences = []
next_tokens = []

for i in range(len(tokens) - sequence_length):
    sequences.append(tokens[i:i + sequence_length])
    # Append the single token that comes right after the sequence
    # This should be a single token, not a sequence
    next_tokens.append(tokens[i + sequence_length])  

# Convert to numpy arrays
x = np.array(sequences)
y = np.array(next_tokens).reshape(-1, 1) 
x_train, x_test, y_train, y_test = prepare_data(x, y)

    # Check if the sizes of x_train and y_train are the same
if len(x_train) != len(y_train):
        raise ValueError(f"The sizes of x_train ({len(x_train)}) and y_train ({len(y_train)}) do not match")

# If the sizes match, proceed with model fitting
try:
    history = model.fit(x_train, y_train, epochs=500, batch_size=64, verbose=1, validation_data=(x_test, y_test))
except Exception as e:
    print(f"An error occurred during model fitting: {e}")
# Now you can call prepare_data with 'x' and 'y'

# Check if the model has already been trained and saved
model_file = 'my_model.h5'
if os.path.isfile(model_file):
    # Load the existing model
    model = load_model(model_file)
else:
    # Create and train the model
    model = create_model(vocab_size, max_length)
    history = model.fit(x_train, y_train, epochs=500, batch_size=64, verbose=1, validation_data=(x_test, y_test))
    # Save the newly trained model
    model.save(model_file)

def generate_text(model, tokenizer, seed_text, num_generated_words):
    output_text = seed_text
    for _ in range(num_generated_words):
        # Tokenize the current seed text
        token_list = tokenizer.texts_to_sequences([output_text])[0]
        # Pad the token list
        token_list = pad_sequences([token_list], maxlen=max_length, padding='pre')
        # Predict the next token
        probabilities = model.predict(token_list, verbose=0)
        predicted = np.argmax(probabilities, axis=-1)
        # Find the word corresponding to the predicted token
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if np.all (index == predicted):
                output_word = word
                break
        # Append the predicted word to the output text
        output_text += " " + output_word
    return output_text
    x_train, y_train, output_text = train_model(tokens, tokenizer)

# Generate new text using the trained model
seed_texts = ["This is", "This is"]  # Replace with actual seed texts
num_generated_words = 10  # Replace with the number of words you want to generate
generated_texts = [generate_text(model, tokenizer, seed_text, num_generated_words) for seed_text in seed_texts]

# Save the generated text to a JSON file
output_file_path = '../data/generated_data.json'
with open(output_file_path, 'a') as f:
    json.dump(generated_texts, f, ensure_ascii=False, indent=4)
