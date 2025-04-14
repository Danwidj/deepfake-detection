import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns
import ast

os.makedirs("../results/visuals", exist_ok=True)


def extract_columns(df):
    return [col for col in df.columns if col not in ['filename', 'fake','feature_length']]

def preprocess_data(df):
    columns_to_parse = extract_columns(df)
    for col in columns_to_parse:
        df[col] = df[col].apply(ast.literal_eval)
        
    return df

def average_segments(seq, num_segments=5):
    k = len(seq) // num_segments
    return [np.mean(seq[i:i+k]) for i in range(0, len(seq), k)][:num_segments]


os.makedirs("../results/visuals", exist_ok=True)

data_path = ["../results/pdd_features.csv","../results/eval_features.csv"]

for path in data_path:
    df = pd.read_csv(path)
    df = preprocess_data(df)
    columns = extract_columns(df)
    
    for col in columns:
        feature = col
        feature_display_name = feature.upper()

        # Check number of frames
        num_frames = len(df[feature][0])

        if num_frames > 5:
            df[f'{feature}_segmented'] = df[feature].apply(lambda x: average_segments(x, 5))
            frame_labels = [f"Segment {i+1}" for i in range(5)]
        else:
            df[f'{feature}_segmented'] = df[feature]
            frame_labels = [f"{i+1}" for i in range(num_frames)]

        # Split and stack
        real_df = df[df['fake'] == 0].copy()
        fake_df = df[df['fake'] == 1].copy()

        real_data = np.stack(real_df[f'{feature}_segmented'].to_numpy())
        fake_data = np.stack(fake_df[f'{feature}_segmented'].to_numpy())

        # Plot
        fig, axs = plt.subplots(1, 2, figsize=(16, 10))

        sns.heatmap(real_data, ax=axs[0], cmap="viridis", cbar=True,
                    xticklabels=frame_labels, yticklabels=real_df['filename'].tolist())
        axs[0].set_title(f"Real Videos - {feature_display_name} Heatmap", fontsize=16, fontweight='bold', color="green")
        axs[0].set_xlabel("Sequence", fontsize=14, fontstyle='italic')
        axs[0].set_ylabel("Video Filename", fontsize=14, fontstyle='italic')

        sns.heatmap(fake_data, ax=axs[1], cmap="viridis", cbar=True,
                    xticklabels=frame_labels, yticklabels=fake_df['filename'].tolist())
        axs[1].set_title(f"Fake Videos - {feature_display_name} Heatmap", fontsize=16, fontweight='bold', color="red")
        axs[1].set_xlabel("Sequence", fontsize=14, fontstyle='italic')
        axs[1].set_ylabel("Video Filename", fontsize=14, fontstyle='italic')

        plt.tight_layout()
        
        # Save the figure
        dataset_name = "pdd" if "pdd" in path else "eval"
        save_path = f"../results/visuals/{feature}_{dataset_name}_heatmap.png"
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()