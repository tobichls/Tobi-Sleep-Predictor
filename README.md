# README for Tobi's Sleep Predictor Project

## Introduction
Welcome to the Sleep Predictor Project! This repository is a showcase of a comprehensive data science endeavor aimed at predicting sleep quality using rich datasets from Fitbit and Google Fit. The project leverages advanced data cleaning, exploratory data analysis, statistical testing, and machine learning techniques. It's a testament to my skills in handling, analyzing, and drawing insights from complex, real-world data.

## Objective
The primary goal of this project is to develop a robust sleep prediction model. By integrating data from wearable technology and external factors, the model aims to understand the determinants of good sleep and predict sleep quality accurately. This work has implications for personal health monitoring and wellness technology development.

## Project Highlights

- **Comprehensive Data Integration**: Merged and analyzed data from Fitbit and Google Fit, demonstrating advanced skills in handling and integrating data from multiple sources.
- **Advanced Data Cleaning Techniques**: Employed sophisticated data cleaning methods including heatmaps for missing data visualization and Multiple Imputation by Chained Equations (MICE).
- **Statistical Analysis and Testing**: Conducted Chi-Square tests, Cramer's V and other statistical analyses.
- **Predictive Modeling**: Developed a sleep quality prediction model using machine learning techniques.
- **Incorporation of External Factors**: Integrated external data sources like weather information to analyse the impact of environmental factors on personal health data.
- **Problem-Solving Approach**: Developed problem-solving abilities in data preprocessing and analysis, a critical skill in data science.
- **Technical Proficiency**: Improved expertise in Python and its key libraries such as Pandas, Numpy, and Scipy.
- **Attention to Data Integrity**: Created unique identifiers for data logs, ensuring data traceability and reliability, a practice that reflects a high standard of data governance.
- **Real-World Application and Relevance**: The project aligns with current health and wellness trends, emphasizing its practicality and relevance in the current data-driven landscape.
- **Effective Documentation**: Maintained clear and detailed documentation of the project workflow and findings, demonstrating the ability to communicate complex information effectively.


## Project Structure and File Descriptions

### Python Scripts

#### 1. `clean_fitbit_data.py`
- **Purpose**: This script meticulously cleans and preprocesses sleep data from Fitbit, ensuring data quality and consistency.
- **Technologies Used**: Python, Pandas, JSON, OS, Datetime
  
#### 2. `clean_gfit_data.py`
- **Purpose**: Processes Google Fit data, emphasizing the handling of data from different sources.
- **Technologies Used**: Python, Pandas, JSON, OS, Random

### Jupyter Notebooks

#### 1. `second_data_cleaning.ipynb`
- **Purpose**: Further refines the combined Fitbit and Google Fit data, preparing it for advanced analytical tasks.
- **Highlights**:
  - Utilizes heatmaps for missing data visualization, showcasing proficiency in data visualization techniques.
  - Employs regression imputation and MICE, demonstrating advanced skills in handling missing data.
  - Conducts Chi-Square tests, reflecting a strong foundation in statistical analysis.
- **Technologies Used**: Python, Pandas

#### 2. `Sleep-Predictor v2.ipynb`
- **Purpose**: This is the crux of the project, where the sleep prediction model is built and evaluated.
- **Highlights**:
  - Incorporates statistical analysis and machine learning algorithms for predictive modeling.
  - Integrates external data like weather, displaying an understanding of the broader impacts on sleep quality.
- **Technologies Used**: Python, Pandas, Scipy, Numpy

## Final Dataset
The culmination of this project is the `Tobi-Sleep-Predictor-Data2` dataset, a meticulously cleaned and enriched compilation of data, ready for high-level analysis and modeling.

## Skills Developed:
- **Data Cleaning and Preprocessing**: Ensuring data quality and usability.
- **Statistical Analysis**: Understanding and applying statistical methods to derive insights.
- **Predictive Modeling**: Developing and tuning models to forecast outcomes.
- **Data Visualization**: Communicating findings effectively through visual means.
- **Problem-Solving**: Addressing complex challenges with innovative solutions.

## Installation and Execution
Please ensure Python and its relevant libraries (Pandas, Numpy, Scipy, etc.) are installed. The scripts and notebooks should be executed in the provided order for optimal results.


