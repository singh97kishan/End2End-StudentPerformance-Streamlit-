import sys
import pickle
import streamlit as st
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

from src.exception import CustomException

st.title("Student Exam Performance Prediction")
input_gender = st.selectbox(
    "Gender", ['male', 'female'])
input_race_ethnicity = st.selectbox(
    "Race or Ethnicity", ['group A', 'group B', 'group C', 'group D'])
input_parental_level_of_education = st.selectbox(
    "Parental level of Education", ["associate's degree", "bachelor's degree", " high school", " master's degree","some college", "some high school"])
input_lunch =st.selectbox(
    "Lunch Type", ["free/reduced", "standard"])
input_test_prepration = st.selectbox(
    "Select Test Course", ["none", "completed"])
input_reading_score =st.number_input(
    "Reading Score (out of 100)", 0, 100)
input_writing_score = st.number_input(
    "Writing Score (out of 100)", 0, 100)

pred_df= CustomData(
    input_gender,
    input_race_ethnicity,
    input_parental_level_of_education,
    input_lunch,
    input_test_prepration,
    input_reading_score,
    input_writing_score
    ).get_data_as_dataframe()

def predict_datapoint(df):
    try:
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(df)
        return results
    except Exception as e:
        raise CustomException(e, sys)
    
if __name__=='__main__':
    if st.button("Predict"):
        st.success(f"Prediction: {predict_datapoint(pred_df)[0]}")