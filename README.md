# HEOG-Derived-SME
Official implementation of the paper:

**HEOG-Derived Slow Eye Movement Detection for Driver Vigilance Monitoring Using Support Vector Machine**

## Overview
This repository contains the implementation of an HEOG-based driver vigilance monitoring framework for detecting slow eye movements (SEMs) associated with driver drowsiness. The proposed framework performs feature preprocessing, feature standardization, hyperparameter optimization, and Support Vector Machine (SVM) classification for distinguishing between alert and drowsy driver states.

## Repository Structure
HEOG-Derived-SME/

│
├── data/                 # Dataset (not included)

├── models/               # Trained models (optional)

├── figures/              # Figures used in the paper

├── src/                  # Source code

├── requirements.txt      # Python dependencies

├── main.py               # Main program

└── README.md

## Requirements
- Python 3.10+
- NumPy
- SciPy
- scikit-learn
- matplotlib
- seaborn


## Dataset
The dataset used in this study was introduced by:
> Jiao Y., Deng Y., Luo Y., Lu B.-L.
> *Driver sleepiness detection from EEG and EOG signals using GAN and LSTM networks.*
> Neurocomputing, 2020.

The dataset is **not distributed** with this repository. Please obtain it from the original authors or the original publication.

The implementation performs:
1. Feature standardization
2. Hyperparameter optimization using GridSearchCV
3. Five-fold cross-validation
4. RBF-SVM training
5. Driver state prediction
6. Performance evaluation


## Contact
Mahade Hasan
GitHub:
https://github.com/Mahade95
