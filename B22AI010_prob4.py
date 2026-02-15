import os
import pandas as pd
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

"""
Course: CSL 7640 (NLU) | Assignment 1
Problem 4: Sports vs Politics Document Classifier
Author: Bhagwan Arsewad | Roll No: B22AI010
"""

def main():
    # 1. Loading the Dataset
    # load_files expects a 'Data' folder with 'politics' and 'sport' subfolders
    data_dir = 'Data' 
    if not os.path.exists(data_dir):
        print(f"Error: Folder '{data_dir}' not found. Please ensure your directory structure is correct.")
        return

    print("Step 1: Loading 928 text documents...")
    dataset = load_files(data_dir, encoding='utf-8', decode_error='ignore')
    
    # 2. Feature Engineering (TF-IDF + Bigrams)
    # We use (1, 2) n-grams to capture phrases like 'maternity pay' or 'champions league'
    print("Step 2: Transforming text into TF-IDF vectors (Bigrams included)...")
    tfidf = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=5000)
    X = tfidf.fit_transform(dataset.data)
    y = dataset.target

    # 3. Data Partitioning
    # 80/20 split as per standard machine learning practices
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Defining Models for Comparison
    models = {
        "Multinomial Naive Bayes": MultinomialNB(),
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Linear SVM": SVC(kernel='linear')
    }

    # 5. Evaluating Models and Printing the Formal Table
    print("\nStep 3: Evaluating Models...")
    print("=" * 65)
    # This header matches your report requirements
    print(f"{'Technique':<25} | {'Accuracy':<8} | {'Prec':<6} | {'Rec':<6} | {'F1':<6}")
    print("-" * 65)

    for name, clf in models.items():
        # Training
        clf.fit(X_train, y_train)
        
        # Prediction
        y_pred = clf.predict(X_test)
        
        # Metrics calculation
        acc = accuracy_score(y_test, y_pred)
        # We use 'weighted' average to account for class distribution
        prec, rec, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
        
        print(f"{name:<25} | {acc:.4f}   | {prec:.2f}   | {rec:.2f}   | {f1:.2f}")

    print("=" * 65)

    # 6. Analysis: Top Indicators (Helps explain the 100% accuracy in the report)
    feature_names = tfidf.get_feature_names_out()
    print("\n--- Top Discriminative Bigrams per Category ---")
    for i, label in enumerate(dataset.target_names):
        class_indices = (y == i)
        row_sum = X[class_indices].sum(axis=0).A1
        top_indices = row_sum.argsort()[-10:][::-1]
        print(f"{label.upper()}: {', '.join([feature_names[idx] for idx in top_indices])}")

if __name__ == "__main__":
    main()