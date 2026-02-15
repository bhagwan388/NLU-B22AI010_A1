
"""
Course: CSL 7640 (Natural Language Understanding)
Assignment: 1 | Problem 3: Naive Bayes from Scratch
Name: Bhagwan Arsewad | Roll Number: B22AI010
"""

import sys
import re
import math
import random
from collections import Counter

def tokenize(text):
    """
    Standard whitespace tokenization as per instructions.
    We convert to lowercase and remove non-alphanumeric characters.
    """
    return re.findall(r'\b\w+\b', text.lower())

class NaiveBayesClassifier:
    def __init__(self):
        # Using separate counters for each sentiment class
        self.counts = {'POSITIVE': Counter(), 'NEGATIVE': Counter()}
        self.total_words = {'POSITIVE': 0, 'NEGATIVE': 0}
        self.class_priors = {'POSITIVE': 0.0, 'NEGATIVE': 0.0}
        self.vocab = set()

    def train(self, pos_data, neg_data):
        """
        Builds the frequency distribution for words in both categories.
        Applies the Bag-of-Words assumption.
        """
        # Calculate Priors: P(Class)
        total_docs = len(pos_data) + len(neg_data)
        self.class_priors['POSITIVE'] = len(pos_data) / total_docs
        self.class_priors['NEGATIVE'] = len(neg_data) / total_docs

        # Build word frequency tables
        for label, data in [('POSITIVE', pos_data), ('NEGATIVE', neg_data)]:
            for sentence in data:
                tokens = tokenize(sentence)
                self.counts[label].update(tokens)
                self.vocab.update(tokens)
                self.total_words[label] += len(tokens)

    def predict(self, sentence):
        """
        Implements the Multinomial Naive Bayes formula with Laplace Smoothing.
        We use log probabilities to prevent arithmetic underflow.
        """
        tokens = tokenize(sentence)
        v_size = len(self.vocab)
        
        # Start with the log of the prior P(C)
        scores = {
            'POSITIVE': math.log(self.class_priors['POSITIVE']),
            'NEGATIVE': math.log(self.class_priors['NEGATIVE'])
        }

        for label in ['POSITIVE', 'NEGATIVE']:
            for word in tokens:
                # We skip words not seen in training as they don't help classification
                if word in self.vocab:
                    # Laplace Smoothing formula: (count + 1) / (total_words + |V|)
                    count = self.counts[label][word]
                    word_prob = (count + 1) / (self.total_words[label] + v_size)
                    scores[label] += math.log(word_prob)
        
        return 'POSITIVE' if scores['POSITIVE'] > scores['NEGATIVE'] else 'NEGATIVE'

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    # 1. Loading the text files
    try:
        pos_lines = load_data('pos.txt')
        neg_lines = load_data('neg.txt')
    except FileNotFoundError:
        print("Error: pos.txt or neg.txt missing in the current directory.")
        return

    # 2. Reasonable Data Split (80% Train, 20% Validation)
    # We shuffle to ensure the split is representative
    random.seed(42) # For reproducible results
    random.shuffle(pos_lines)
    random.shuffle(neg_lines)

    pos_split = int(0.8 * len(pos_lines))
    neg_split = int(0.8 * len(neg_lines))

    train_pos, val_pos = pos_lines[:pos_split], pos_lines[pos_split:]
    train_neg, val_neg = neg_lines[:neg_split], neg_lines[neg_split:]

    # 3. Training
    print(f"Training on {len(train_pos) + len(train_neg)} sentences...")
    clf = NaiveBayesClassifier()
    clf.train(train_pos, train_neg)

    # 4. Validation (Optional check to see if the model works)
    correct = 0
    total = len(val_pos) + len(val_neg)
    for s in val_pos:
        if clf.predict(s) == 'POSITIVE': correct += 1
    for s in val_neg:
        if clf.predict(s) == 'NEGATIVE': correct += 1
    
    print(f"Validation Accuracy: {(correct/total)*100:.2f}%")

    # 5. Interactive Mode
    print("\n--- Sentiment Classifier (Naive Bayes) ---")
    print("Enter a sentence to test sentiment (Type 'exit' to stop).")
    
    while True:
        user_input = input("\n>> ")
        if user_input.lower() == 'exit':
            break
        
        result = clf.predict(user_input)
        print(f"Prediction: {result}")

if __name__ == "__main__":
    main()