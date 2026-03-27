# NewsGuard - Fake News Detection (Mini Project)

## What this project is
 NLP project to classify news as **Fake** or **Real** using text. This repo is a clean structure with placeholders so you can fill in each part step by step.

## Quick start
1. Put your dataset CSV in `data/raw/` (example: `fake_news.csv`).
   Dataset link:
   ```
   https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification
   ```
2. Update the path in `src/config.py` if your filename is different.
3. Work file by file following the guide below.
4. (Optional) Run the Streamlit UI: `streamlit run app.py`

## Team assignment (4 people)
1. Preprocessing and data handling: `data/`, `src/preprocessing.py`, `notebooks/01_data_exploration.ipynb`, `notebooks/02_preprocessing.ipynb`
2. XGBoost model: `src/features.py`, `src/models/xgboost_model.py`, `src/train_xgboost.py`, `notebooks/03_xgboost.ipynb`
3. TextCNN model: `src/models/textcnn_model.py`, `src/train_textcnn.py`, `notebooks/04_textcnn.ipynb`
4. UI and results: `app.py`, `results/`, `report/`

## Project map (what each part is for)

**data/**
- `data/raw/` : original dataset file.
- `data/processed/` : cleaned dataset after preprocessing.

**notebooks/**
- `01_data_exploration.ipynb` : explore dataset (size, classes, stats).
- `02_preprocessing.ipynb` : clean text and save processed data.
- `03_xgboost.ipynb` : train and evaluate XGBoost.
- `04_textcnn.ipynb` : space for TextCNN (if required).

**src/**
- `src/config.py` : paths and global settings.
- `src/preprocessing.py` : text cleaning functions.
- `src/features.py` : BoW / TF-IDF feature extraction.
- `src/models/xgboost_model.py` : XGBoost model code.
- `src/models/textcnn_model.py` : TextCNN model code (optional).
- `src/evaluation.py` : metrics (accuracy, precision, recall, F1, confusion matrix).
- `src/train_xgboost.py` : training script for XGBoost.
- `src/train_textcnn.py` : training script for TextCNN.
- `src/predict.py` : predict Fake/Real from new text.

**results/**
- Save trained models and charts here.
- `results/models/` is where model files should be saved so the UI can load them later.

**report/**
- Report and presentation files.

**app.py**
- Streamlit UI placeholder (connect your model later).

## Simple workflow
1. Explore the dataset in `notebooks/01_data_exploration.ipynb`.
2. Clean and save data in `notebooks/02_preprocessing.ipynb`.
3. Build features in `src/features.py`.
4. Train XGBoost in `src/train_xgboost.py`.
5. Evaluate in `src/evaluation.py`.
6. (Optional) Add TextCNN if required.
7. Use `src/predict.py` for new text.

## Model files for the UI
Save trained model files in `results/models/` so the Streamlit UI can load them later.
Suggested names:
```
results/models/xgboost_model.pkl
results/models/textcnn_model.*
```

## Notes
- Keep preprocessing consistent between training and prediction.
- Add evaluation charts to `results/charts/`.
- Write your report in `report/`.
