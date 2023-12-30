# README for Tobi's Sleep Predictor Project

## Introduction
Welcome to the Sleep Predictor Project! This repository showcases my comprehensive data science endeavor aimed at predicting sleep quality using rich datasets from Fitbit and Google Fit. The project leverages advanced data cleaning, exploratory data analysis, statistical testing, and machine learning techniques, demonstrating my ability to handle, analyze, and draw insights from complex, real-world data.

## Objective
The primary goal of this project is to develop a robust sleep prediction model. By integrating data from wearable technology and external factors, I aim to understand the determinants of good sleep and predict sleep quality accurately. This work is important as it allows me to monitor my personal health and wellness through technology development.

## Project Highlights

- **Comprehensive Data Integration**: Merged and analyzed data from Fitbit and Google Fit, demonstrating advanced skills in handling and integrating data from multiple sources.
- **Advanced Data Cleaning Techniques**: Employed sophisticated data cleaning methods including heatmaps for missing data visualization and Multiple Imputation by Chained Equations (MICE).
- **Statistical Analysis and Testing**: Conducted Chi-Square tests, Cramer's V, and other statistical analyses.
- **Predictive Modeling**: Developed a sleep quality prediction model using machine learning techniques.
- **Incorporation of External Factors**: Integrated external data sources like weather information to analyze the impact of environmental factors on personal health data.
- **Problem-Solving Approach**: Showcased problem-solving abilities in data preprocessing and analysis, a critical skill in data science.
- **Technical Proficiency**: Demonstrated expertise in Python and its key libraries such as Pandas, Numpy, and Scipy.
- **Attention to Data Integrity**: Created unique identifiers for data logs, ensuring data traceability and reliability.
- **Real-World Application and Relevance**: The project aligns with current health and wellness trends, emphasizing its practicality and relevance.
- **Effective Documentation**: Maintained clear and detailed documentation of the project workflow and findings.

## (Some) Challenges Faced and my Solutions

### Data Cleaning Challenges:
1. **Incomplete Sleep Data**: The Fitbit data export lacked specific sleep duration data.
   - **Solution**: Developed a Python script to process extra Fitbit data files, filling missing values and adding new rows as needed.

2. **Inconsistent Data Formats**: Google Fit sleep data was in a per-session format, unlike Fitbit's single-file format.
   - **Solution**: Created a Python program to standardize Google Fit data, ensuring consistency with Fitbit data format.

3. **Potential Duplicate Data**: Additional Fitbit data in split file format may have had overlaps with the main dataset.
   - **Solution**: Implemented a data verification step to identify and handle potential duplicates.

4. **Data Volume Discrepancy**: Google Fit had significantly fewer data rows compared to Fitbit.
   - **Solution**: Employed data augmentation techniques to balance the datasets.

5. **Merging Diverse Data Sources**: Needed to integrate Google Fit daily activity metrics with the main dataset to explore correlations.
   - **Solution**: Used data merging techniques to combine datasets and performed exploratory analysis to identify key correlations.

6. **Missing Values in Key Columns**: Observed numerous missing values in selected Google Fit columns.
   - **Solution**: Applied predictive modeling and Multiple Imputation by Chained Equations (MICE) to intelligently fill missing values.

### Advanced Data Cleaning:
- **Redundant Column**: Discovered a column with no values across the dataset.
  - **Solution**: Confirmed the redundancy through Jupyter Notebook analysis and removed the column.

### Predictive Modeling Challenges:
- **Imputation Inefficiencies**: MICE IterativeImputer was not effectively filling missing values.
  - **Solution**: Developed a custom MICE approach, adjusted post-imputation based on Fitbit guidelines, and sorted data by date for more accurate imputation.

## Project Structure and File Descriptions

### Python Scripts

#### 1. `clean_fitbit_data.py`
- **Purpose**: This script meticulously cleans and preprocesses sleep data from Fitbit, focusing on data normalization and formatting to ensure quality and consistency.
- **Technologies Used**: Python, Pandas, JSON, OS, Datetime

#### 2. `clean_gfit_data.py`
- **Purpose**: Processes Google Fit data, standardizing and cleaning it for uniformity with the Fitbit data.
- **Technologies Used**: Python, Pandas, JSON, OS, Random

### Jupyter Notebooks

#### 1. `second_data_cleaning.ipynb`
- **Purpose**: Further refines the combined Fitbit and Google Fit data, preparing it for advanced analytical tasks.
- **Highlights**:
  - Utilizes heatmaps for missing data visualization.
  - Employs regression imputation and MICE for sophisticated missing data handling.
  - Conducts Chi-Square tests for in-depth statistical analysis.
- **Technologies Used**: Python, Pandas, OS, Json, Matplotlib, Seaborn
- **Notes**:
  - I have a personal goal of sleeping 8 hours each night so I included this goal in my data cleaning process:
      Created a column in my dataset called sleep_deviation and it represents how much my sleep duration for a particular night deviates from the 8 hour mark.
      Included this column in training my custom MICE to fill in null datapoints in the dataset so it will predict values with that knowledge.

#### 2. `Sleep-Predictor v2.ipynb`
- **Purpose**: Perform analysis of data and more visualisations.
- **Highlights**:
  - Features advanced machine learning algorithms for predictive modeling.
  - Integrates external weather data for a comprehensive analysis of sleep quality.
- **Technologies Used**: Python, Pandas, Scipy, Numpy, Matplotlib, Seaborn, Json
- **Notes**:
  - Used zscore standardisation for stress level column creation.

## Final Dataset
The culmination of this project is the `Tobi-Sleep-Predictor-Data2` dataset, a meticulously cleaned and enriched compilation of data, ready for high-level analysis and modeling.

## Skills I Developed:
- **Data Cleaning and Preprocessing**: Enhanced the quality and usability of complex datasets.
- **Statistical Analysis**: Applied statistical methods to extract meaningful insights from data.
- **Predictive Modeling**: Developed and refined models to accurately forecast outcomes.
- **Data Visualization**: Used visual tools to effectively communicate findings.
- **Problem-Solving**: Addressed and resolved complex data challenges.

## Installation and Execution
Please ensure Python and its relevant libraries (Pandas, Numpy, Scipy, etc.) are installed. Execute the scripts and notebooks in the provided order for optimal results.

## Contact Information
For more information or to discuss this project further, please feel free to connect with me on [LinkedIn](<http://www.linkedin.com/in/tobi-fakoya>).
