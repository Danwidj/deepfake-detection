# Deep Fake Detection (DFD) Dataset

This directory contains the Deep Fake Detection dataset from Kaggle. The dataset is used for training and evaluating deepfake detection models.

## Dataset Information

- Source: [Kaggle - Deep Fake Detection Dataset](https://www.kaggle.com/datasets/sanikatiwarekar/deep-fake-detection-dfd-entire-original-dataset/)
- Description: A collection of real and fake (deepfake) images for training and testing deepfake detection models
- License: Please check the original dataset's terms of use on Kaggle

## Dataset Organization

- Original sequences: Located in `DFD_original_sequences/` directory
- Manipulated sequences: Located in `DFD_manipulated_sequences/` directory
- Balanced dataset: Located in `balanced_dataset/` directory (created after running the balancing script)

## Running the Dataset Balancing Script

The `balance_DFD.ipynb` notebook is used to create a balanced version of the dataset by matching original videos with their manipulated counterparts. Here's how to run it:

1. Make sure you have the following Python packages installed:

   ```bash
   pip install jupyter
   ```

2. Open the notebook:

   ```bash
   jupyter notebook balance_DFD.ipynb
   ```

3. Run the cells in sequence. The notebook will:

   - Analyze the dataset structure
   - Match original videos with their manipulated versions
   - Create a balanced dataset in the `balanced_dataset/` directory

4. The balanced dataset will be organized as follows:
   ```
   balanced_dataset/
   ├── original/      # Contains original videos
   └── manipulated/   # Contains manipulated videos
   ```

## Notes

- The original dataset contains 364 original videos and 3068 manipulated videos
- The balancing process matches each original video with its corresponding manipulated versions
- The balanced dataset ensures a more even distribution between original and manipulated content
- Make sure you have enough disk space before running the balancing script
- The process might take some time depending on the size of your dataset

## Download Instructions

1. Go to the [dataset page on Kaggle](https://www.kaggle.com/datasets/sanikatiwarekar/deep-fake-detection-dfd-entire-original-dataset/)
2. Click the "Download" button
3. Extract the downloaded zip file into this directory (`data/DFD/`)
4. Run the balancing script to create a balanced version of the dataset
