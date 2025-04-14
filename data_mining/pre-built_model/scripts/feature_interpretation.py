import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os
import cv2

# --- Load features and labels ---
X = np.load("test.npy")     # shape (N, D)
y = np.load("labels.npy")   # shape (N,)
frame_base_path = "./test"

folder_list = sorted(os.listdir(frame_base_path))

# --- Standardize for stability ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ============================================================
# PART 1: Feature Probing - Which dimensions are most predictive
# ============================================================

# Train logistic regression
clf = LogisticRegression(max_iter=1000)
clf.fit(X_scaled, y)

# --- Sort and split by sign ---
weights = clf.coef_[0]
feature_indices = np.arange(len(weights))

# Top 10 for fake (most negative weights)
fake_indices = np.argsort(weights)[:10]
print("\n🤖 Top 10 Features Predictive of FAKE Videos:")
for i in fake_indices:
    print(f"Feature {i}: Weight = {weights[i]:.4f}")

# Top 10 for real (most positive weights)
real_indices = np.argsort(weights)[-10:][::-1]
print("\n👤 Top 10 Features Predictive of REAL Videos:")
for i in real_indices:
    print(f"Feature {i}: Weight = {weights[i]:.4f}")

# Optional bar chart
plt.figure(figsize=(10, 4))
plt.bar([f"F{i}" for i in fake_indices], weights[fake_indices], label="Fake", color='red')
plt.bar([f"F{i}" for i in real_indices], weights[real_indices], label="Real", color='blue')
plt.axhline(0, color='gray', linestyle='--')
plt.ylabel("LogReg Weight")
plt.title("Top Features Predictive of Real vs Fake - Pre-trained Model")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ============================================================
# PART 2: Similarity Search - Find similar real/fake pairs
# ============================================================
def find_similar_pairs(X, y, top_k=3):
    sim_matrix = cosine_similarity(X)
    pairs = []
    for i in range(len(X)):
        for j in range(i + 1, len(X)):
            if y[i] != y[j]:  # Only compare real vs fake
                pairs.append((i, j, sim_matrix[i, j]))
    pairs = sorted(pairs, key=lambda x: -x[2])[:top_k]
    return pairs

print("\n🔁 Finding most similar real-fake pairs...")
similar_pairs = find_similar_pairs(X_scaled, y)

for idx, (i, j, sim) in enumerate(similar_pairs):
    real_idx = i if y[i] == 1 else j
    fake_idx = j if y[j] == 0 else i
    print(f"Pair {idx+1}: Real = {folder_list[real_idx]}, Fake = {folder_list[fake_idx]} — Cosine sim: {sim:.4f}")

# ============================================================
# PART 3: Optional — Show representative frames
# ============================================================
def show_frames(video_indices, title="", base_path="./test"):
    plt.figure(figsize=(15, 4))
    for i, idx in enumerate(video_indices):
        folder = os.path.join(base_path, folder_list[idx])
        if not os.path.exists(folder):
            print(f"⚠️ Folder not found: {folder}")
            continue

        frame_files = sorted([f for f in os.listdir(folder) if f.endswith(".jpg")])
        if not frame_files:
            print(f"⚠️ No .jpg frames found in: {folder}")
            continue

        mid_frame_path = os.path.join(folder, frame_files[len(frame_files) // 2])
        img = cv2.imread(mid_frame_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.subplot(1, len(video_indices), i + 1)
        plt.imshow(img)
        plt.title(f"{folder_list[idx]}")
        plt.axis("off")

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

# === Get indices to visualize ===
to_show = []
for (i, j, _) in similar_pairs[:2]:
    to_show.extend([i, j])
to_show = list(set(to_show))  # remove duplicates

# === Display frames ===
if to_show:
    show_frames(to_show, title="Top Real-Fake Similar Pairs")
else:
    print("⚠️ No similar pairs found to visualize.")
