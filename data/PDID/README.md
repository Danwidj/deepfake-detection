# PDID Dataset

This dataset is based on the research paper: "Merging AI Incidents Research with Political Misinformation Research: Introducing the Political Deepfakes Incidents Database" by Christina P. Walker, Daniel S. Schiff, and Kaylyn Jackson Schiff (2024). [Link to paper](https://arxiv.org/html/2409.15319v1)

This directory contains the PDID (Politician Deepfake Identification Dataset) used for training and testing deepfake detection models.

## Dataset Source

The dataset is stored in a SharePoint location containing two subfolders:

- Real Politician Videos
- Fake Politician Videos

Access the dataset here: [Link](https://smu-my.sharepoint.com/personal/adrian_tok_2023_scis_smu_edu_sg/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fadrian%5Ftok%5F2023%5Fscis%5Fsmu%5Fedu%5Fsg%2FDocuments%2FDeepfake%20Detection%20Videos&ga=1)

## Download Instructions

1. Access the SharePoint link above using your SMU credentials
2. Navigate to the dataset folder
3. Download the contents of both subfolders:
   - Download all files from the "Real Politician Videos" subfolder
   - Download all files from the "Fake Politician Videos" subfolder
4. Save the downloaded files to their respective directories in this folder:
   - Save real videos to `data/PDID/real_videos/`
   - Save fake videos to `data/PDID/deepfakes/`

## Directory Structure

```
data/PDID/
├── real_videos/     # Real politician videos
├── deepfakes/       # Deepfake samples
└── README.md        # This file
```

## Notes

- Make sure you have sufficient storage space for the dataset
- The download process might take some time depending on your internet connection
- Keep the original file names to maintain consistency
