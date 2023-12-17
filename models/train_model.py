import sys
import os
import json
import numpy as np
from model import create_model, prepare_data
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.callbacks import Callback
from tensorflow.keras.preprocessing.text import Tokenizer


# Set the paths for scripts and data
sys.path.append('../scripts/')
sys.path.append('../data/')

from load_data import load_json, extract_text_data
from process_data import tokenize_text_data

file_path = '../data/data.json'
data = load_json(file_path)
text_data = extract_text_data(data)
tokens, tokenizer = tokenize_text_data(text_data)
print('Loading data...')

max_length = 1114  # Maximum length of input sequence
# Set the maximum number of words to consider as features
max_vocab = 192  # Adjust this value according to your needs

tokenizer = Tokenizer(num_words=max_vocab, oov_token="<OOV>")
tokenizer.fit_on_texts(text_data)
vocab_size = len(tokenizer.word_index) + 1  # Vocabulary size

# Assuming 'tokens' is a list of all tokens in the dataset
sequence_length = 10  # The length of each input sequence
sequences = []
next_tokens = []

for i in range(len(tokens) - sequence_length - 1):
    sequences.append(tokens[i:i + sequence_length])
    next_tokens.append(tokens[i + 1:i + sequence_length + 1])

# Convert to numpy arrays
x = np.array(sequences)
y = np.array(next_tokens)


# Now you can call prepare_data with 'x' and 'y'
x_train, y_train, x_test, y_test = prepare_data(x, y)


# Create the model
model = create_model(vocab_size, max_length)


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
            if np.all(index == predicted):
                output_word = word
                break
        # Append the predicted word to the output text
        output_text += " " + output_word
    return output_text

    #Train the model
    
    x_train, y_train, output_text = train_model(tokens, tokenizer)

# Generate new text using the trained model
seed_texts = ["This is", "This is"]  # Replace with actual seed texts
num_generated_words = 100  # Replace with the number of words you want to generate
generated_texts = [generate_text(model, tokenizer, seed_text, num_generated_words) for seed_text in seed_texts]

x_train, y_train, x_test, y_test = prepare_data(x, y)

def model_fit(x_train, y_train, x_test, y_test, model):
    epoch_display = EpochDisplay()
    history = model.fit(x_train, y_train, epochs = 500, batch_size=32, verbose=1, validation_data=(x_test, y_test))
    return history

class EpochDisplay(Callback):
    def on_epoch_begin(self, epoch, logs=None):
        print(f"Starting epoch {epoch+1}")

        history = model_fit(x_train, y_train, x_test, y_test, model)

# Save the generated text to a JSON file
output_file_path = '../data/generated_data.json'
with open(output_file_path, 'w') as f:
    json.dump(generated_texts, f, ensure_ascii=False, indent=4)