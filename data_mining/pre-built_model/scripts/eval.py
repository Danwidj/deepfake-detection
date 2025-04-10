import numpy as np
import faiss
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import precision_recall_curve, confusion_matrix, ConfusionMatrixDisplay
from tqdm import tqdm
import argparse

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

parser = argparse.ArgumentParser(description='')
parser.add_argument('--real_root', help='path to the real data (train set)')
parser.add_argument('--test_root', help='path to the test set')
parser.add_argument('--labels_root', help='path to the test labels')
args = parser.parse_args()

train_set = np.load(args.real_root, allow_pickle=True).astype(np.float32)
test_set = np.load(args.test_root, allow_pickle=True).astype(np.float32)
labels = np.load(args.labels_root, allow_pickle=True)

# Ensure that the lengths of train_set, test_set, and labels match
print(f"Train set size: {train_set.shape}")
print(f"Test set size: {test_set.shape}")
print(f"Labels size: {labels.shape}")

index = faiss.IndexFlatL2(train_set.shape[1])
index.add(train_set)
k_value = 5
D, _ = index.search(test_set, k_value)
distances = np.sum(D, axis=1)

roc_auc_val = roc_auc_score(labels, distances)
ap = average_precision_score(labels, distances)
print(f'AP: {ap*100}, AUC: {roc_auc_val*100}')

# ----------------------
# Plot: AP and AUC
# ----------------------
plt.bar(['AP', 'AUC'], [ap * 100, roc_auc_val * 100], color=['skyblue', 'orange'])
plt.title('Evaluation Metrics - Pre-trained Model')
plt.ylabel('Score (%)')
plt.ylim(0, 100)
plt.grid(True, axis='y')
plt.show()

# ----------------------
# Plot: Distance distributions
# ----------------------
real_distances = distances[labels == 1]
fake_distances = distances[labels == 0]

sns.kdeplot(real_distances, label='Real', fill=True, color='green')
sns.kdeplot(fake_distances, label='Fake', fill=True, color='red')
plt.title("Distance Distribution: Real vs Fake - Pre-trained Model")
plt.xlabel("FAISS L2 Distance")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()

# ----------------------
# ROC Curve
# ----------------------
fpr, tpr, _ = roc_curve(labels, distances)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------
# Precision-Recall Curve
# ----------------------
precision, recall, _ = precision_recall_curve(labels, distances)
plt.figure()
plt.plot(recall, precision, lw=2, color='purple', label=f'AP = {ap:.2f}')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------
# Confusion Matrix
# ----------------------
# You can use a threshold to convert distances to binary predictions.
# Lower distance = more similar to real = label 1, so we'll invert it for prediction scoring.
# threshold = np.median(distances)
# predictions = (distances < threshold).astype(int)  # Label as real if distance is below median

# Find the best threshold using Youden’s J statistic (maximizing TPR - FPR)
fpr, tpr, thresholds = roc_curve(labels, distances)
j_scores = tpr - fpr
best_thresh_idx = np.argmax(j_scores)
best_threshold = thresholds[best_thresh_idx]
print(f"Optimal threshold based on ROC curve: {best_threshold:.4f}")

predictions = (distances < best_threshold).astype(int)

cm = confusion_matrix(labels, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fake", "Real"])
disp.plot(cmap='Blues', values_format='d')
plt.title("Confusion Matrix (Threshold = Median Distance)")
plt.grid(False)
plt.tight_layout()
plt.show()