from pathlib import Path

class Config:
  RANDOM_SEED = 90
  ASSETS_PATH = Path("C:/Data Science/project-6-Pharmaceutical/Rossmann-Sales/models/")
  REPO = "~/Documents/Rossmann-Pharmaceuticals-Sales-Prediction"
  DATASET_FILE_PATH = "data/train.csv"
  DATASET_PATH = ASSETS_PATH / "data"
  FEATURES_PATH = ASSETS_PATH / "features"
  MODELS_PATH = ASSETS_PATH / "models"
  
