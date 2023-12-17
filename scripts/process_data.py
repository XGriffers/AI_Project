from keras.preprocessing.text import Tokenizer

def tokenize_text_data(text_data):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(text_data)
    tokens = tokenizer.texts_to_sequences(text_data)
    tokens = [item for sublist in tokens for item in sublist]
    return tokens, tokenizer

def calculate_vocab_size_and_max_length(tokenizer, text_data):
    vocab_size = len(tokenizer.word_index) + 1
    max_length = max(len(text) for text in text_data)
    return vocab_size, max_length