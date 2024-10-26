import pandas as pd
import random

# Define columns for the autism dataset
columns = ["Age (Years)", "Communication Score", "Social Interaction", 
           "Repetitive Behaviors", "Family History", "Recommendation"]

# Generate a dataset with ages from 2 years to 50 years
data = []
for age in range(2, 51):  # Age in years
    communication_score = random.choice(["Low", "Moderate", "High"])
    social_interaction = random.choice(["Poor", "Average", "Good"])
    repetitive_behaviors = random.choice(["Yes", "No"])
    family_history = random.choice(["Yes", "No"])
    
    # Simple logic for Recommendation based on age and scores
    if communication_score == "Low" and social_interaction == "Poor":
        recommendation = "Early Intervention"
    elif communication_score == "Moderate" and social_interaction == "Average":
        recommendation = "Monitor"
    else:
        recommendation = "Full Evaluation"
    
    # Append row to the data list
    data.append([age, communication_score, social_interaction, repetitive_behaviors, family_history, recommendation])

# Create DataFrame
autism_dataset = pd.DataFrame(data, columns=columns)

# Save to CSV
autism_dataset.to_csv("data/autism_data.csv", index=False)

# Display the first few rows of the dataset
print(autism_dataset.head(10))
