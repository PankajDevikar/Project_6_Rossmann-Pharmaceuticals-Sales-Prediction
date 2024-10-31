import os
import sys
import pandas as pd
from pathlib import Path
from config import Config
from sklearn.preprocessing import LabelEncoder
from file_handler import FileHandler

# Append the scripts directory to sys.path
sys.path.append(os.path.abspath(os.path.join('C://Data Science//project-6-Pharmaceutical//Rossmann-Sales//scripts')))

# Create directories if they do not exist
Config.FEATURES_PATH.mkdir(parents=True, exist_ok=True)

# Initialize the file handler
file_handler = FileHandler()

# Read CSV files using Path objects
train_df = file_handler.read_csv(Config.DATASET_PATH / "data new/train.csv")
test_df = file_handler.read_csv(Config.DATASET_PATH / "data/test.csv")
store_df = file_handler.read_csv(Config.DATASET_PATH / "data new/store.csv")

def merge(df, store):
    df_merge = pd.merge(df, store, on='Store')
    return df_merge

def get_part_of_month(day):
    if day < 10:
        return 0
    elif day < 20:
        return 1
    else:
        return 2

def extract_test_features(df):
    df = merge(df, store_df)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['DayOfMonth'] = df['Date'].dt.day
    df['WeekOfYear'] = df['Date'].dt.isocalendar()['week']  # Updated to use isocalendar
    df['weekday'] = df['DayOfWeek'].apply(lambda x: 0 if (x in [6, 7]) else 1)

    df = df[df['Open'] == 1]
    df["part_of_month"] = df["DayOfMonth"].apply(get_part_of_month)

    # Label encoding
    lb_state = LabelEncoder()
    lb_assortment = LabelEncoder()
    lb_store = LabelEncoder()

    df['StateHoliday'] = lb_state.fit_transform(df['StateHoliday'])
    df['Assortment'] = lb_assortment.fit_transform(df['Assortment'])
    df['StoreType'] = lb_store.fit_transform(df['StoreType'])

    df = df.drop(columns=['Id', 'PromoInterval', 'Date'], axis=1)
    return df

def extract_features(df):
    df = df[df['Open'] == 1]
    df["part_of_month"] = df["DayOfMonth"].apply(get_part_of_month)

    # Label encoding
    lb_state = LabelEncoder()
    lb_assortment = LabelEncoder()
    lb_store = LabelEncoder()

    df['StateHoliday'] = lb_state.fit_transform(df['StateHoliday'])
    df['Assortment'] = lb_assortment.fit_transform(df['Assortment'])
    df['StoreType'] = lb_store.fit_transform(df['StoreType'])

    df = df.drop(columns=['Sales', 'Customers', 'PromoInterval', 'Date'], axis=1)
    return df

def extract_sales(df):
    df = df[df['Open'] == 1]
    return df[["Sales"]]

def extract_customers(df):
    df = df[df['Open'] == 1]
    return df[["Customers"]]

# Extract features and targets
train_features = extract_features(train_df)
test_features = extract_test_features(test_df)

target_sales = extract_sales(train_df)
target_customers = extract_customers(train_df)

# Save the features and targets to CSV files
train_features.to_csv(Config.FEATURES_PATH / "C:\Data Science\project-6-Pharmaceutical\Rossmann-Sales\features\train_features.csv", index=False)
test_features.to_csv(Config.FEATURES_PATH / "C:\Data Science\project-6-Pharmaceutical\Rossmann-Sales\features\test_features.csv", index=False)

target_sales.to_csv(Config.FEATURES_PATH / "C:\Data Science\project-6-Pharmaceutical\Rossmann-Sales\features\target_sales.csv", index=False)
target_customers.to_csv(Config.FEATURES_PATH / "C:\Data Science\project-6-Pharmaceutical\Rossmann-Sales\features\target_customers.csv", index=False)
