# Deepfake Detection Project

This repository contains the code and resources for IS424 AY24/25 Data Mining and Business Analysis Project G1T3, focusing on deepfake detection using various machine learning approaches.

## Project Overview

This project aims to develop and compare different methods for detecting deepfake videos and images. The repository includes implementations of traditional machine learning methods, pre-built deep learning models, and custom deep learning architectures.

## Project Structure

```
├── data/                  # Dataset storage. Currently it is empty
├── EDA/                   # Exploratory Data Analysis notebooks and scripts
├── pre-processing/        # Data preprocessing utilities
├── data_mining/          # Main model implementations
│   ├── traditional_method/  # Traditional ML approaches
│   ├── pre-built_model/    # Pre-trained deep learning models
│   └── custom_model/       # Custom deep learning architectures
└── venv/                 # Python virtual environment
```

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/deepfake-detection.git
cd deepfake-detection
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The project provides multiple approaches for deepfake detection:

1. **Traditional Methods**: Located in `data_mining/traditional_method/`
2. **Pre-built Models**: Located in `data_mining/pre-built_model/`
3. **Custom Models**: Located in `data_mining/custom_model/`

Each approach has its own documentation and usage instructions within its respective directory.

## Contributing

This project is part of IS424 AY24/25 Data Mining and Business Analysis course. For any questions or contributions, please contact the project team.
