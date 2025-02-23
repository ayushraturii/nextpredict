from tensorflow.keras.models import load_model as keras_load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle

# Load tokenizer (assumes it's saved during training)



def load_trained_model(path):
    """Load a pre-trained model from the specified path."""
    return keras_load_model(path)

def predict_next_word(style,model, text, max_sequence_len=20, top_k=3):
    """Predict the next word based on the input text."""

    with open(f'models/{style}_tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    
    
    sequence = tokenizer.texts_to_sequences([text])[0]
    padded_sequence = pad_sequences([sequence], maxlen=max_sequence_len, padding='pre')
    predictions = model.predict(padded_sequence)
    top_indices = predictions[0].argsort()[-top_k:][::-1]
    top_words = [word for word, index in tokenizer.word_index.items() if index in top_indices]
    return top_words
