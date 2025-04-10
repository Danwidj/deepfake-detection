import numpy as np
import os

# Define the paths for real and fake video folders
train_root = './test'

# Initialize lists to store all features and labels
all_labels = []
all_features = []

# Function to load the features and create corresponding labels
def process_video_folder(video_folder, label):
    # Load the feature.npy file in the current video folder
    feature_file = os.path.join(video_folder, 'features.npy')
    if os.path.exists(feature_file):
        features = np.load(feature_file)  # Load the features

        # Aggregate the frame-level features to one per video
        video_feature = np.mean(features, axis=0)
        
        all_features.append(video_feature)
        all_labels.append(label)
    else:
        print(f"Feature file not found in {video_folder}")

# Process the train videos
for video_folder in os.listdir(train_root):
    video_folder_path = os.path.join(train_root, video_folder)
    
    # Check if the folder is a directory
    if os.path.isdir(video_folder_path):
        if 'real' in video_folder.lower():
            label = 1  # Label 1 for real videos
        elif 'fake' in video_folder.lower():
            label = 0  # Label 0 for fake videos
        else:
            continue  # Skip any folders that do not match real or fake naming
        
        # Process the folder and assign labels
        process_video_folder(video_folder_path, label)

# Convert lists to numpy arrays
all_features = np.vstack(all_features)
all_labels = np.array(all_labels)

# Save the labels to labels.npy
np.save('labels.npy', all_labels)

print(f"Labels saved to 'labels.npy' with {len(all_labels)} labels.")


