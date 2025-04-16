# PDD (Public Deepfake Dataset)

This directory contains the Public Deepfake Dataset (PDD) for deepfake detection research.

## Dataset Information

- Source: Public Deepfake Dataset
- Source Paper: [Deepfake Detection: A Comprehensive Study](https://ceur-ws.org/Vol-2942/paper3.pdf)
- Description: A collection of real and fake (deepfake) images for training and testing deepfake detection models
- License: Please check the original dataset's terms of use

## Setup and Download Instructions

1. Install required dependencies:

   ```bash
   pip install yt-dlp
   ```

2. Run the scrape script to download videos:

   ```bash
   python scrape.py
   ```

   This will download a collection of YouTube videos that will be used for the dataset.

3. The script will download videos to the current directory. Each video will be saved with its original title.

## Dataset Organization

- `fake/`: Contains manipulated/deepfake images
- `real/`: Contains authentic images

## Notes

- Make sure you have enough disk space before running the script
- The download process might take some time depending on your internet connection
- Ensure you have accepted YouTube's terms of service before downloading videos
- The script uses yt-dlp for downloading videos, which is a more reliable alternative to youtube-dl
