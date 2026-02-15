# CSL 7640: Natural Language Understanding - Assignment 1
**Author:** Bhagwan Arsewad  
**Roll Number:** B22AI010  
**Institution:** IIT Jodhpur  
**GitHub Repository:** [NLU-B22AI010_A1](https://github.com/bhagwan388/NLU-B22AI010_A1)

---

## 📋 Project Overview
This repository contains the full implementation for Assignment 1 of the CSL 7640 (NLU) course. The assignment involves rule-based NLP, subword tokenization (BPE), and comparative analysis of machine learning models for news classification.

---

## 📂 Deliverables

| Task | Filename | Description |
| :--- | :--- | :--- |
| **Problem 1** | `B22AI010_prob1.py` | Regex-based chatbot (Reggy++) with age and mood detection. |
| | `B22AI010_prob1.log` | Execution log showing multiple chatbot transcripts. |
| | `B22AI010_prob1.txt` | 300-500 word reflection on chatbot naturalness. |
| **Problem 2** | `B22AI010_prob2.py` | Byte Pair Encoding (BPE) implemented from scratch. |
| **Problem 3** | `B22AI010_prob3.py` | Naive Bayes Sentiment Classifier with Laplace smoothing. |
| **Problem 4** | `B22AI010_prob4.pdf` | **6-Page Detailed Technical Report**. |
| | `B22AI010_prob4.py` | Sports vs. Politics News Classification Benchmark. |

---

## 🚀 Execution Instructions

### Problem 2: BPE Tokenization
The script takes the number of merges $k$ and the corpus file as command-line arguments:
```bash
python B22AI010_prob2.py 10 corpus.txt

```

### Problem 4: News Classification

Run the benchmark script to compare Naive Bayes, Logistic Regression, and SVM:

```bash
python B22AI010_prob4.py

```

---

## 📊 Experimental Results

### Problem 2: BPE Subword Learning

The algorithm successfully learned subword units by iteratively merging the most frequent character pairs.

<p align="center">
<img src="https://github.com/user-attachments/assets/d407dab6-862a-4933-9914-c9d9731a7a4e" width="800" alt="BPE Output Results">
</p>

### Problem 4: Model Benchmarking

All three machine learning models achieved 100% accuracy on the test set, indicating the linear separability of the Politics and Sports domains.

<p align="center">
<img src="https://www.google.com/search?q=https://github.com/bhagwan388/NLU-B22AI010_A1/blob/main/result_photo.png%3Fraw%3Dtrue" width="800" alt="Problem 4 Results">
</p>

| Model | Accuracy | Precision | Recall | F1-Score |
| --- | --- | --- | --- | --- |
| **Naive Bayes** | 1.0000 | 1.00 | 1.00 | 1.00 |
| **Logistic Regression** | 1.0000 | 1.00 | 1.00 | 1.00 |
| **Linear SVM** | 1.0000 | 1.00 | 1.00 | 1.00 |

---

## 📜 Originality Statement

All code has been implemented independently following the course guidelines. No external NLP libraries were used for the scratch implementations (Problem 1, 2, and 3).
