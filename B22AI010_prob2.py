import sys
import re
from collections import Counter, defaultdict

"""
Author: Bhagwan Arsewad (B22AI010)
Task: Byte Pair Encoding (BPE) implementation.
This script helps handle out-of-vocabulary words by merging frequent character pairs.
"""

def get_stats(vocab):
    """
    Goes through the vocabulary and counts how many times 
    each pair of characters appears next to each other.
    """
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i], symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, v_in):
    """
    Once we find the most frequent pair, we 'glue' them together 
    everywhere they appear in our vocabulary.
    """
    v_out = {}
    # We escape the pair to handle special characters safely in Regex
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        # Replace the pair 'A B' with 'AB'
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

def main():
    # We need exactly 3 arguments: script name, k, and the file
    if len(sys.argv) < 3:
        print("Usage: python B22AI010_prob2.py <k_merges> <corpus_file>")
        return

    # k is the number of times we perform the merge operation
    k = int(sys.argv[1])
    corpus_path = sys.argv[2]

    try:
        with open(corpus_path, 'r', encoding='utf-8') as f:
            # We split by whitespace to get individual words
            text = f.read().split()
    except FileNotFoundError:
        print(f"Error: {corpus_path} not found. Check your file path!")
        return

    # We start by splitting words into characters and adding a stop token </w>
    # This helps the algorithm know where a word ends.
    vocab = Counter([' '.join(list(word)) + ' </w>' for word in text])

    print(f"--- Starting BPE with {k} merges ---")
    
    for i in range(k):
        pairs = get_stats(vocab)
        if not pairs:
            break
        
        # Find the pair that appears most often
        best = max(pairs, key=pairs.get)
        vocab = merge_vocab(best, vocab)
        print(f"Iteration {i+1}: Merging {best} (Count: {pairs[best]})")

    print("\n--- Final Vocabulary Sample ---")
    # Show a few examples of what the tokens look like now
    for word, freq in list(vocab.items())[:5]:
        print(f"Tokenized Word: {word} | Frequency: {freq}")

if __name__ == "__main__":
    main()