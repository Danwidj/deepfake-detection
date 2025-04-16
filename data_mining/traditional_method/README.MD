# Obtaining Results using Traditional Classification Methods

This project focuses on building and evaluating machine learning models to detect deepfake content. Using labeled datasets of authentic and deepfake samples, we train classifiers, assess their performance, and visualize key evaluation metrics.

---

## Project Structure

All key files are located in the `scripts/` folder:

- `scripts/classification.ipynb` — Jupyter Notebook containing all code for:
  - Data preprocessing
  - Model training and evaluation
  - Visualizations (confusion matrix etc.)
- `scripts/pdd_features.csv` — Extracted features for the **training set**.
- `scripts/eval_features.csv` — Extracted features for the **test set**.

- `README.md` — You're here!

---

## Features

- Preprocessing of features using standard scaling
- Training multiple classifiers (e.g., Logistic Regression, Random Forest, etc.)
- Evaluation using:
  - Accuracy
  - Precision / Recall / F1-Score
  - AUC
  - Confusion Matrix (with TP as Predicted: Deepfake / Actual: Deepfake)

---

## Getting Started

### Prerequisites

Make sure you have Python 3.7+ and `pip` installed. 

Then, install the necessary packages:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn ast