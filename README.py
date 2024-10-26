# Autism Clinical Decision Support System (CDSS)

## Project Overview
This project is a Clinical Decision Support System (CDSS) designed to assist in recommending interventions for autism based on specific behavioral indicators. The system analyzes patient data and suggests recommendations such as "Early Intervention," "Monitor," or "Full Evaluation" based on communication, social interaction, repetitive behaviors, and family history.

## Dataset
- **File**: `autism_data.csv`
- **Attributes**:
  - **Age (Years)**: Patient’s age in years.
  - **Communication Score**: Rated as "Low," "Moderate," or "High."
  - **Social Interaction**: Rated as "Poor," "Average," or "Good."
  - **Repetitive Behaviors**: Indicates if repetitive behaviors are observed (Yes/No).
  - **Family History**: Indicates if there is a family history of autism (Yes/No).
  - **Generated Recommendation**: System-generated recommendation based on patient data.

## Project Workflow
1. **Data Loading**: The system loads patient data from `autism_data.csv`.
2. **Recommendation Logic**:
   - Recommendations are based on predefined rules analyzing communication and social interaction scores.
3. **Visualization**:
   - **Distribution of Recommendations**: A bar chart that shows the overall distribution of recommendations across all patients.
   - **Recommendations by Age Group**: A stacked bar chart showing how recommendations vary across different age groups.

## Visualizations
- **Distribution of Recommendations**: Shows how patients are classified across different recommendation categories.
- **Recommendations by Age Group**: Provides insight into how recommendations are distributed by patient age.

## Getting Started
1. Clone this repository and navigate to the project directory.
2. Install dependencies by running:
   ```bash
   pip install pandas matplotlib


   ## Future Improvements

Guys, I have outlined several possible enhancements to expand the capabilities of this Clinical Decision Support System (CDSS) for autism care. These improvements will focus on increasing accuracy, leveraging machine learning, broadening the dataset, and making the system user-friendly. I would love for us to each contribute to these areas to further develop the project.

### 1. Enhance the Recommendation Logic with Data-Driven Insights
   - **Goal**: Move beyond basic rule-based logic by analyzing patterns in the data.
   - **Actions**:
     - **Data Analysis**: Examine correlations between attributes like communication score, age, and family history to refine recommendation logic.
     - **Weighted Conditions**: Adjust the rules to emphasize specific conditions (e.g., "Low" communication score with "Poor" social interaction might strongly indicate "Early Intervention").
     - **Statistical Testing**: Use hypothesis testing to validate the impact of different attributes on outcomes.

### 2. Integrate Machine Learning Models for Complex Decision-Making
   - **Goal**: Implement machine learning (ML) models to predict recommendations based on patient data patterns.
   - **Actions**:
     - **Data Preparation**: Split the dataset into training and testing sets.
     - **Model Selection**: Try classification models such as Decision Trees, Random Forests, or Support Vector Machines (SVM).
     - **Model Training**: Train a model using `scikit-learn` to predict recommendations based on age, communication score, and other attributes.
     - **Evaluate Performance**: Assess model accuracy and fine-tune as needed.
     - **Implement Predictions**: Use the ML model’s predictions alongside the rule-based system for more accurate recommendations.

### 3. Expand the Dataset for a More Comprehensive CDSS
   - **Goal**: Broaden the dataset to make the system’s recommendations more reliable and diverse.
   - **Actions**:
     - **Sourcing Additional Data**: Explore publicly available autism-related datasets to enhance the model.
     - **Data Augmentation**: Create a synthetic dataset or add variations to simulate a larger data pool.
     - **Refine Logic**: Analyze new data patterns to refine the decision-making criteria.

### 4. Add User-Friendly Interfaces
   - **Goal**: Create a user-friendly interface for clinicians or caregivers.
   - **Actions**:
     - **Interface Development**: Use frameworks like Flask or Django to build a web interface for patient data input.
     - **Visualization Integration**: Embed interactive charts and graphs in the interface for better data insights.
     - **Testing and Deployment**: Test the interface for usability and deploy it on a local or cloud server.

These improvements will help make the CDSS more accurate, scalable, and user-friendly. So contributions to any of these areas are welcome to help elevate this project to the next level!

