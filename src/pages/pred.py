# imports
import os
import sys
import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt
import streamlit as st
import awesome_streamlit as ast
from keras.models import load_model

# Corrected path for Windows
sys.path.append(os.path.abspath(os.path.join(r'C:\Data Science\project-6-Pharmaceutical\Rossmann-Sales\scripts')))
from file_handler import FileHandler

def write():
    """Used to write the page in the app.py file"""
    st.header('Prediction on Test Data')
    
    # Initialize FileHandler
    file_handler = FileHandler()
    df = file_handler.read_csv(r'features/test_features.csv')
    test_df = file_handler.read_csv(r'src/data/test.csv')
    
    # Display Sample Test Data
    st.markdown('### Sample Test Data Input')
    st.write(test_df.head(10))
    
    # Load the Model
    import os

    model_path = r'C:\Data Science\project-6-Pharmaceutical\Rossmann-Sales\models\LSTM_sales_weights_2024-10-31-08-24-31.weights.h5'
    if os.path.exists(model_path):
        print("Model file exists.")
    else:
        print("Model file does not exist at the specified path.")


    try:
        model = load_model(model_path)  # Use load_model for Keras models
        st.write(f"Loaded model type: {type(model)}")  # Verify model type
        
        # Make Predictions
        y_preds = model.predict(df)  # Ensure df is in the right shape for predictions
        prediction_df = df.copy()
        prediction_df["Pred_sales"] = y_preds
        st.markdown('### Sample Prediction Output')
        st.write(prediction_df["Pred_sales"].head(10))
    
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return  # Exit the function if the model fails to load
    
    # SHAP Analysis
    try:
        explainer = shap.DeepExplainer(model, df)
        shap_values = explainer.shap_values(df)

        # Feature Importance Plots
        st.header('Feature Importance')

        plt.title('Feature Importance based on SHAP values')
        shap.summary_plot(shap_values, df)
        st.pyplot(bbox_inches='tight')
        plt.close()  # Prevent overlapping plots
        
        plt.title('Feature Importance based on SHAP values (Bar)')
        shap.summary_plot(shap_values, df, plot_type="bar")
        st.pyplot(bbox_inches='tight')
        plt.close()  # Prevent overlapping plots
        
    except Exception as e:
        st.error(f"Error during SHAP analysis: {str(e)}")

    st.write('---')
