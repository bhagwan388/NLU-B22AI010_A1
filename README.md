# CSL 7640: NLU - Problem 4: News Classification Benchmark (PROBLEM 4: SPORTS OR POLITICS)
**Author:** Bhagwan Arsewad  
**Roll Number:** B22AI010  
**Project:** Sports vs. Politics News Classifier

---

## 📋 Problem Description
This task involves building a robust text classifier to distinguish between **Sports** and **Politics** news articles. The project benchmarks three distinct machine learning architectures to evaluate their performance on domain-specific text data.

---

## 🛠️ System Requirements
To execute the classification script, ensure you have the following Python libraries installed:

```bash
pip install scikit-learn pandas

```

* **Python Version**: 3.8+
* **Dependencies**: `scikit-learn` (for models), `pandas` (for data handling), `re` (for preprocessing).

---

## 🚀 Execution Instructions

Ensure your dataset is in the correct directory, then run the benchmark script:

```bash
python B22AI010_prob4.py

```

The script will perform the following steps:

1. **Preprocessing**: Tokenization, lowercasing, and removal of special characters.
2. **Feature Extraction**: Converting text to numerical vectors using `TfidfVectorizer`.
3. **Training & Evaluation**: Training Naive Bayes, Logistic Regression, and Linear SVM models.
4. **Results**: Outputting a detailed classification report for each model.

---

## 📊 Performance Results

All three models achieved perfect separation of the classes, resulting in **100% accuracy** across the test set. This suggests that the vocabulary used in the Politics and Sports datasets is highly distinct.

<p align="center">
<img src="https://www.google.com/search?q=https://github.com/bhagwan388/NLU-B22AI010_A1/blob/main/result_photo.png%3Fraw%3Dtrue" width="850" alt="Problem 4 Terminal Results">





<em>Figure: Terminal output showing 1.000 accuracy for all benchmarked models.</em>
</p>

| Model | Accuracy | Precision | Recall | F1-Score |
| --- | --- | --- | --- | --- |
| **Naive Bayes** | 1.0000 | 1.00 | 1.00 | 1.00 |
| **Logistic Regression** | 1.0000 | 1.00 | 1.00 | 1.00 |
| **Linear SVM** | 1.0000 | 1.00 | 1.00 | 1.00 |

---

## 📂 Included Deliverables

* `B22AI010_prob4.py`: The Python source code for the classifier.
* `B22AI010_prob4.pdf`: A comprehensive 6-page report detailing the methodology, data distribution, and results analysis.
