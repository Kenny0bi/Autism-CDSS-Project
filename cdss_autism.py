import pandas as pd
import matplotlib.pyplot as plt

# Load the autism dataset
data = pd.read_csv('data/autism_data.csv')

# Function to determine the recommendation based on specific conditions
def make_recommendation(row):
    # If communication is low and social interaction is poor, suggest early intervention
    if row['Communication Score'] == "Low" and row['Social Interaction'] == "Poor":
        return "Early Intervention"
    # If communication is moderate and social interaction is average, suggest monitoring
    elif row['Communication Score'] == "Moderate" and row['Social Interaction'] == "Average":
        return "Monitor"
    # For other combinations, recommend a full evaluation
    else:
        return "Full Evaluation"

# Apply the recommendation function to each row in the dataset
data['Generated Recommendation'] = data.apply(make_recommendation, axis=1)

# Display the first few rows with generated recommendations to verify
print(data[['Age (Years)', 'Communication Score', 'Social Interaction', 
           'Repetitive Behaviors', 'Family History', 'Generated Recommendation']].head(10))

# Plot: General distribution of recommendations
plt.figure(figsize=(8, 6))
data['Generated Recommendation'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Recommendations')
plt.xlabel('Recommendation')
plt.ylabel('Number of Patients')
plt.xticks(rotation=45)
plt.show()

# Create age groups for patients (0-10, 11-20, ..., 41-50 years)
data['Age Group'] = pd.cut(data['Age (Years)'], bins=[0, 10, 20, 30, 40, 50], labels=['0-10', '11-20', '21-30', '31-40', '41-50'])

# Plot: Recommendations by age group as a stacked bar chart
plt.figure(figsize=(10, 6))
data.groupby('Age Group')['Generated Recommendation'].value_counts().unstack().plot(kind='bar', stacked=True, color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Recommendations by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Patients')
plt.xticks(rotation=0)
plt.legend(title='Recommendation')
plt.show()
