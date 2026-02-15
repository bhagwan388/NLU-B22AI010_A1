# CSL 7640: NLU - Problem 4: News Classification Benchmark
**Author:** Bhagwan Arsewad  
**Roll Number:** B22AI010  
**Project:** Sports vs. Politics News Classifier

---

## 📋 Problem Description
This task involves building a robust text classifier to distinguish between **Sports** and **Politics** news articles. The project benchmarks three distinct machine learning architectures to evaluate their performance on domain-specific text data from the BBC News archive.

---

## 📊 Dataset & Preprocessing
Understanding the data distribution is key to interpreting the high performance of these models.

| Metric | Statistics |
| :--- | :--- |
| **Total Samples** | ~800 Articles |
| **Classes** | Sports (50%), Politics (50%) |
| **Avg. Document Length** | ~400 words |
| **Vocabulary Distinctiveness** | High (Low overlap between domain terms) |

### Preprocessing Pipeline
1. **Case Folding**: All text converted to lowercase to reduce vocabulary sparsity.
2. **Regex Cleaning**: Removal of punctuation, special characters, and numbers.
3. **TF-IDF Vectorization**: Term Frequency-Inverse Document Frequency was used to weigh domain-specific words (like "ballot" or "wicket") more heavily than common stop words.

---

## 🔬 Methodology & Models
Unlike baseline models, this project benchmarks three robust architectures to ensure results are consistent across different mathematical approaches:

1. **Multinomial Naive Bayes**: A probabilistic approach that works exceptionally well with word frequency features.
2. **Logistic Regression**: A discriminative model that finds the optimal linear boundary between categories.
3. **Linear SVM**: Designed to find the maximum margin hyperplane, ensuring the best possible separation.

---

## 🛠️ System Requirements
```bash
pip install scikit-learn pandas

```

* **Python Version**: 3.8+
* **Dependencies**: `scikit-learn`, `pandas`, `re`.

---

## 🚀 Execution Instructions

Ensure your dataset is in the root directory, then run:

```bash
python B22AI010_prob4.py

```

The script will automatically perform preprocessing, feature extraction, and output a detailed classification report for each model.

---

## 📈 Performance Results

All three models achieved perfect separation of the classes, resulting in **100% accuracy** across the test set. This is attributed to the **High Class Separability**—the vocabulary used in Sports (e.g., *match, league*) rarely intersects with Politics (e.g., *election, government*), making the task linearly separable.

<p align="center">
<img src="Screenshot 2026-02-06 024223.png" width="850" alt="Problem 4 Terminal Results">





<em>Figure: Terminal output showing 1.000 accuracy for all benchmarked models.</em>
</p>

| Model | Accuracy | Precision | Recall | F1-Score |
| --- | --- | --- | --- | --- |
| **Naive Bayes** | 1.0000 | 1.00 | 1.00 | 1.00 |
| **Logistic Regression** | 1.0000 | 1.00 | 1.00 | 1.00 |
| **Linear SVM** | 1.0000 | 1.00 | 1.00 | 1.00 |

---

## 📂 Included Deliverables

* `B22AI010_prob4.py`: Python source code for the classifier.
* `B22AI010_prob4.pdf`: A comprehensive 6-page report detailing the methodology, data distribution, and results analysis.
