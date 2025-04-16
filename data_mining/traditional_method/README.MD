# Obtaining results using traditional classification methods

This project focuses on building and evaluating machine learning models to detect deepfake content. Using labeled datasets of authentic and deepfake samples, we train classifiers, assess their performance, and visualize key evaluation metrics.

---

## Project Structure

- `classification.ipynb` — Jupyter Notebook containing all code for data processing, model training, evaluation, and visualization.
- `pdd_features.csv` — Extracted data for train set
- `eval_features.csv` — Extracted data for test set
- `README.md` — You're here!

---

## Features

- Preprocessing of features using standard scaling
- Training multiple classifiers (e.g., Logistic Regression, Random Forest, etc.)
- Evaluation using:
  - Accuracy
  - Precision / Recall / F1-Score
  - ROC Curve and AUC
  - Confusion Matrix (with TP as Predicted: Deepfake / Actual: Deepfake)

---

## Getting Started

### Prerequisites

Make sure you have Python 3.7+ and `pip` installed. 

Then, install the necessary packages:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn ast