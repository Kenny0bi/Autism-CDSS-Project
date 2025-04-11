# Autism Clinical Decision Support System (CDSS)

This project implements a rule-based Clinical Decision Support System (CDSS) designed to assist in recommending appropriate interventions for individuals with potential signs of autism. Based on behavioral indicators and patient data, the system generates recommendations such as **Early Intervention**, **Monitor**, or **Full Evaluation**.

---

## 🧠 Project Features

- Rule-based logic that considers:
  - Communication score
  - Social interaction
  - Repetitive behaviors
  - Family history
- Generates tailored recommendations based on combined indicators
- Produces visualizations to support clinical insights:
  - Distribution of recommendations
  - Recommendations grouped by age

---

## 📊 Dataset

**File:** `autism_data.csv`  
**Attributes:**
- `Age (Years)`
- `Communication Score`: (Low / Moderate / High)
- `Social Interaction`: (Poor / Average / Good)
- `Repetitive Behaviors`: (Yes / No)
- `Family History`: (Yes / No)

---

## 📈 Visualizations

- **Distribution of Recommendations**  
  A bar chart showing the number of patients receiving each type of recommendation.
- **Recommendations by Age Group**  
  A stacked bar chart showing how recommendations vary across age brackets.

---

## 🧪 How It Works

1. Patient data is loaded from `autism_data.csv`
2. A custom function analyzes communication and social scores to assign a recommendation:
   - **Low communication + Poor social interaction** → Early Intervention
   - **Moderate communication + Average social interaction** → Monitor
   - All other combinations → Full Evaluation
3. Visual outputs are saved as `.png` charts

---

## ▶️ How to Run

Install dependencies:
```bash
pip install pandas matplotlib

Run the script: python autism_cdss.py

Outputs:

distribution_of_recommendations.png

recommendations_by_age_group.png

🚀 Future Improvements
1. Enhance the Recommendation Logic with Data-Driven Insights
Analyze patterns in the data to move beyond simple rule-based logic

Apply statistical testing to validate the impact of different attributes

Introduce weighted rules based on data correlations

2. Integrate Machine Learning Models for Complex Decision-Making
Implement classifiers such as Decision Trees or Random Forests using scikit-learn

Train the model on available patient data to predict recommendations

Compare ML outputs with rule-based logic to enhance accuracy

3. Expand the Dataset for Broader Coverage
Incorporate additional public autism datasets to improve reliability

Augment data synthetically for better generalization

Adapt decision logic to reflect broader clinical diversity

4. Add a User-Friendly Interface
Develop a web app using Flask or Django for clinicians or caregivers

Allow interactive data entry and display personalized recommendations

Embed visualizations directly into the user interface
