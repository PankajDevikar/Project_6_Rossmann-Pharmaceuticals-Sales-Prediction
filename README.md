# Rossmann Pharmaceuticals Sales Prediction


## Table of Contents
- [Rossmann Pharmaceuticals Sales Prediction](#rossmann-pharmaceuticals-sales-prediction)
- [Overview](#overview)
- [Scenario](#scenario)
- [Approach](#approach)
- [Project Structure](#project-structure)
  - [data](#data)
  - [models](#models)
  - [notebooks](#notebooks)
  - [scripts](#scripts)
  - [tests](#tests)
  - [logs](#logs)
  - [root folder](#root-folder)
- [Installation guide](#installation-guide)
  

## Overview

This project aims to develop a robust forecasting model to predict future sales for Rossmann Pharmaceuticals stores. By accurately forecasting sales up to six weeks in advance, we aim to support the finance team and individual store managers in planning and optimizing resources.


## Scenario

As a Machine Learning Engineer at Rossmann Pharmaceuticals, you're tasked with forecasting sales across multiple stores in various cities. Currently, store managers rely on their personal experience and judgment to estimate sales. The data team has identified essential factors, including promotions, competition, holidays, seasonality, and locality, to improve the accuracy of sales predictions. The goal is to build an end-to-end solution that delivers these predictions to the finance team's analysts.


## Approach

The project workflow includes:
1. Exploration of customer purchasing behavior
2. Prediction of store sales
3. Implementing a machine learning model
4. Experimenting with a deep learning approach
5. Serving the model predictions via a web interface
   

## Project Structure

The repository is organized as follows:

### data
- Directory to store the dataset in CSV format.

### models
- Directory for saving model pickle files.

### notebooks
- **EDA.ipynb**: Jupyter notebook for exploratory data analysis.
  

### scripts
- **app_logger.py**: Handles logging throughout the project.
- **file_handler.py**: Contains functions for reading and writing CSV, pickle, and other file formats.
- **df_cleaner.py**: Script for cleaning and preprocessing pandas DataFrames.
- **df_selector.py**: Script for selecting specific data subsets from DataFrames.
- **df_visualizer.py**: Contains functions for visualizing data from DataFrames.
- **df_outlier_handler.py**: Script for handling outliers in DataFrames.

### tests
- Folder containing unit tests for the scripts.

### logs
- Directory for storing log files. If it doesn’t exist, it will be created automatically when logging begins.

### root folder
- **requirements.txt**: Lists the project dependencies.
- **travis.yml**: Travis CI configuration file.
- **setup.py**: Configuration file for installing the scripts as a package.
- **README.md**: Contains an overview and instructions for the project.

## Installation guide

To set up the project locally, follow these steps:

```bash
git clone [https://github.com/PankajDevikar/Project_6_Rossmann-Pharmaceuticals-Sales-Prediction]
cd Rossmann-Pharmaceuticals-Sales-Prediction
pip install -r requirements.txt
