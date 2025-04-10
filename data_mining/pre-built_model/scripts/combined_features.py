import numpy as np
import os

# Directory where your video folders with features.npy are located
input_root = "./test"
output_file = "test.npy"

# List to hold all the features
all_features = []

# Walk through the directory to find each features.npy
for root, dirs, files in os.walk(input_root):
    for file in files:
        if file == "features.npy":
            feature_path = os.path.join(root, file)
            print(f"Loading features from {feature_path}")
            
            # Load the features.npy file
            features = np.load(feature_path)
            
            # Append to the list of all features
            mean_feat = np.mean(features, axis=0)
            max_feat = np.max(features, axis=0)
            std_feat = np.std(features, axis=0)
            video_feature = np.concatenate([mean_feat, max_feat, std_feat])
            all_features.append(video_feature)

# Stack all the features into one single array (this assumes the shapes are consistent)
combined_features = np.vstack(all_features)

# Save the combined features into a single .npy file
np.save(output_file, combined_features)

print(f"Combined features saved to {output_file}")
