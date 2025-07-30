### **📊 Exploratory Data Analysis and Prediction: Tourism Sector in Tanzania**

## 📌 Project Overview

Tourism is one of Tanzania’s largest economic drivers, known for its rich wildlife, cultural heritage, and world-class destinations. This project performs **Exploratory Data Analysis (EDA)** on tourism data to extract insights about visitor trends and develops a **classification model** to predict tourism outcomes such as visitor flow categories and market segments.

The results aim to empower policymakers, stakeholders, and tourism boards to make **evidence-based decisions** for sustainable growth of the sector.

---

## 🎯 Objectives

1. **Exploratory Data Analysis (EDA):**

   - Study **visitor demographics**, **spending patterns**, and **seasonal trends**.
   - Analyze **tour package preferences** and **popular activities**.
   - Identify **top source countries** for tourists.

2. **Predictive Modeling:**

   - Build a **classification model** to predict:

     - Tourist flow categories (e.g., **"High"**, **"Medium"**, **"Low"**).
     - Tourist segmentation based on origin or package selection.

   - Provide data-driven insights for strategic planning.

---

## 📂 Dataset Description

| Column Name        | Description                                                             |
| ------------------ | ----------------------------------------------------------------------- |
| `id`               | Unique identifier for each tourist                                      |
| `country`          | Country of origin of the tourist                                        |
| `age_group`        | Age group category of the tourist                                       |
| `travel_with`      | Relation of people the tourist traveled with                            |
| `total_female`     | Total number of females in the travel group                             |
| `total_male`       | Total number of males in the travel group                               |
| `purpose`          | Purpose of visiting Tanzania                                            |
| `main_activity`    | Main activity undertaken during the visit                               |
| `info_source`      | Source of information about Tanzania tourism                            |
| `tour_arrangement` | Tour arrangement (e.g., self-arranged, travel agency)                   |
| `package_services` | Services included in the package (transport, accommodation, food, etc.) |
| `nights_stayed`    | Total number of nights stayed (Mainland + Zanzibar)                     |
| `payment_mode`     | Payment method used for tourism services                                |
| `first_trip_tz`    | Indicates if it was the tourist's first trip to Tanzania                |
| `most_impressing`  | What impressed the tourist the most                                     |
| `total_cost`       | Total expenditure of the tourist (TZS currency)                         |

---

## 🔧 Data Preprocessing

- Fixed column naming inconsistencies (e.g., `infor_source → info_source`).
- Created **`nights_stayed`**: sum of nights spent in mainland and Zanzibar.
- Combined package-related columns into **`package_services`** as a readable string.
- Dropped redundant columns after feature engineering.

---

## 📊 EDA Coverage

- Distribution of tourists by **age group, country, and travel companions**.
- Analysis of **purpose of visit** and **main activities**.
- Spending analysis using **`total_cost`**.
- Seasonal and stay-duration patterns.
- **Package preferences** (e.g., transport, accommodation, sightseeing).
- Visualization of top source markets.

---

## 🛠 Tools and Libraries

- **Python 3.x**
- **Pandas** (data cleaning and manipulation)
- **Matplotlib** (visualizations)

---

## 🔮 Predictive Modeling Approach

- **Type of Problem**: Classification
- **Target Variable Examples**:

  - Tourist flow level (**High/Medium/Low**) based on seasonal data.
  - Tourist market segment based on country or package choice.

- Potential Models:

  - Logistic Regression
  - Random Forest Classifier
  - Gradient Boosting (XGBoost/LightGBM)

---

## 📈 Expected Insights

- Identify **peak seasons** and low visitor periods for strategic planning.
- Recognize **high-spending tourist segments** to optimize revenue.
- Understand package service preferences for targeted offerings.
- Provide predictive insights to help resource allocation and marketing campaigns.

---

## 📜 License

This project is for **educational and analytical purposes**. Data may be subject to local tourism authority rights.

---

Would you like me to **add a "Sample Visualizations Section"** (with example matplotlib charts like tourist distribution by country, spending histogram, etc.) in this README?
