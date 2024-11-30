# **Used Car Analytics**

## **1. Title and Author**

### Project Title: **Used Car Analytics**

- **Prepared for**: UMBC Data Science Master’s Capstone  
  **Advisor**: Dr. Chaojie (Jay) Wang  
- **Author**: Kaushik Manjunatha  

### **Links**
- [LinkedIn](https://www.linkedin.com/in/kaushikm97/)  
- [Presentation Slides](https://docs.google.com/presentation/d/1b8btsZQoy73bZ8BdWUShzpqZzj7Zi9y4/edit?usp=share_link&ouid=115650794338613440123&rtpof=true&sd=true)  
- YouTube: Coming Soon  

---

## **2. Background**

### **Industry Overview**
- **Market Size**: $1.6 trillion in the U.S. (2023)  
- **Sales Channels**: Dealerships, Private Sales, Online Platforms  

### **Personal Motivation**
- **Challenge**: Pricing confusion during a personal car search.  
- **Insights**: No reliable pricing mechanism; relied on word of mouth.  

### **Significance**
- Tackles the **pricing uncertainty** faced by buyers and sellers alike.  

### **Research Questions**
1. **Prediction Accuracy**:  
   Can machine learning models outperform traditional pricing heuristics, especially for electric, gasoline, and hybrid vehicles?  
2. **Depreciation Analysis**:  
   How does depreciation vary across car makes and models over time?  

### **Future Scope**
1. **Maintenance Cost Prediction**:  
   Can machine learning predict the maintenance costs of used cars?

---

## **3. Data**

- **Data Source**: [Cars.com](https://cars.com)  
- **Data Size**: 2.9 MB  
- **Shape**: 14,420 rows × 15 columns  
- **Description**: Each row represents a single car listing from a dealership.  
- **Target Variable**: `Price_usd`  

### **Data Dictionary**
![Data Dictionary](https://github.com/user-attachments/assets/9d760765-6348-40f9-a9fa-08f276a3ea31)

---

## **4. Project Implementation Plan**
![Project Plan](https://github.com/user-attachments/assets/cad41f8e-9b98-4881-819f-d907600d9840)

---

## **5. Data Pre-Processing**

1. Merged multiple files categorized by region, fuel type, and transmission type.  
2. Split "Make," "Model," and "Year" into separate fields.  
3. Calculated car age from the current year.  
4. Converted `Price`, `Reviews`, and `Mileage` to numeric types, handling non-numeric entries.  
5. Extracted `State` and `County` from the `Location` field.  
6. Removed duplicate records based on matching specifications and pricing.

---

## **6. Exploratory Data Analysis (EDA)**

### **Dealer Ratings**
![Ratings](https://github.com/user-attachments/assets/605ff72d-395f-4b0c-8f64-0683a4492c11)  
- Majority of ratings fall between 4 and 5.  
- Poor-rated dealerships represent a small fraction.

### **Car Age Distribution**
![Car Age](https://github.com/user-attachments/assets/42f5c83a-4015-4854-85c9-1252923df9d0)  
- Median car age: 3 years.  
- Outliers include vintage cars (up to 69 years old).  

### **Median Prices by Make**
![Median Prices](https://github.com/user-attachments/assets/069b3820-ed7a-4e29-b561-ef6381a5f66e)  
- Luxury brands (Ferrari, Rolls-Royce) show the highest median prices.  
- Common brands (Ford, Toyota) are priced significantly lower.

### **Vintage Cars**
![Vintage Cars](https://github.com/user-attachments/assets/29c803eb-bc77-4b95-882c-ce28a4edfb60)  
- Higher prices for 1950s–1960s cars due to rarity and collectibility.  

### **Transmission Types**
![Transmission Prices](https://github.com/user-attachments/assets/383f2884-9677-4ce8-827d-89ffb7a01917)  
- Automatic transmissions exhibit the highest price variability.  
- Manual and CVT transmissions have compact price distributions.

### **Fuel Types**

<img width="374" alt="image" src="https://github.com/user-attachments/assets/d9790877-ef4e-4e33-8301-6b1e24166f28">

- Gasoline and hybrid cars exhibit the widest range of prices
- Diesel and electric vehicles show more concentrated price distributions
- automatic transmissions exhibit the highest price variability
- manual and CVT transmissions have more compact price distributions


### **Mileage vs. Age**
![Mileage vs Age](https://github.com/user-attachments/assets/ffb2bff9-d3fb-4336-b186-a98e434dacbd)  
- Older cars (20–40 years) typically have 100k–200k mileage.  
- Some outliers include newer cars with unusually high mileage.

---

## **7. Feature Engineering**

1. **Missing Value Imputation**: Replaced missing values with the mean of the respective category (e.g., by `Transmission`, `Fuel Type`).  
2. **Categorical Feature Encoding**:  
   - One-Hot Encoding for linear models.  
   - Label Encoding for tree-based models.  

---

## **8. Model Training**

### **Initial Attempt**
- **Dataset Split**: 80% Train, 20% Test  

**Tree-Based Models**:  
- Decision Tree: R² = 0.6178  
- Random Forest: R² = 0.7904  
- XGBoost: R² = 0.8223  
- Gradient Boosting: R² = 0.7618  

**Linear Models**:  
- Linear Regression: R² = -51310135364.8435  

### **Addressing Linear Model Issues**
- Handled multicollinearity (`Age`, `Year`, `Dealer`).  
- Managed non-linear relationships (e.g., `User Reviews`, `Dealership Rating`).  

**Improved Linear Regression**: R² = -0.7568  

### **Ensemble Techniques**
1. **Stacking Regressor** (Linear Meta-Model + Tree-Based Base Models):  
   - Without tuning: R² = 0.8397  
   - With tuning: R² = 0.8473  

2. **Stacking Regressor with Other Meta Models**:  
   - Ridge: R² = 0.8726  
   - Lasso: R² = 0.8732  

### **Best Model**
- **XGBoost**:  
  Parameters: `n_estimators=100`, `max_depth=7`, `learning_rate=0.1`  
  Performance: R² = 0.8349  

---

## **9. Application of Trained Models**

### **Application**  
[Used Car Price Prediction App](https://used-cars-price-prediction-usa.streamlit.app)  

![App Screenshot](https://github.com/user-attachments/assets/fd5363d3-8fda-48ad-9bd1-5d4c81e011bb)

---

## **10. Conclusion**

- **Significant Factors**: Mileage, Age, Make, and Model.  
- **Best Model**: XGBoost (R² = 0.8349).  

---

## **11. References**

- [Using Selenium for Web Scraping](https://brightdata.com/blog/how-tos/using-selenium-for-web-scraping)
