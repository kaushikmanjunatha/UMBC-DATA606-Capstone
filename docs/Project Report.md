 
## 1. Title and Author

- USED CAR ANALYTICS

- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Kaushik Manjunatha
- [LinkedIn](https://www.linkedin.com/in/kaushikm97/)
- [Presentation Slides](https://github.com/kaushikmanjunatha/UMBC-DATA606-Capstone/blob/main/docs/Kaushik%20Manjunatha%20Project%20Presentation.pptx)
- Youtube
    
## 2. Background

- **Total Market Value:** $1.6 trillion in the U.S. as of 2023
- **Market Channels :** Dealerships , Private Sales , Online Platforms

**Personal Experience with Used Car Pricing**
- Pricing was overwhelming when searching for a used car.
- No reliable method to verify correct pricing.
- Relied on word of mouth for pricing validation.


**Why does it matter?**
- This project addresses the common challenge of pricing uncertainty for both buyers and sellers.


**Research questions**
1. Prediction Accuracy
Can machine learning models outperform traditional pricing heuristics in accurately predicting used car values, especially in high-demand vehicle categories like electric, Gasoline and hybrid models?
2. Depreciation Analysis
How does the depreciation rate vary across different car makes and models over time?

**Future Scope :**
1. Maintenance Cost Prediction
Can we predict the maintenance costs for the used cars?


## 3. Data 

Describe the datasets you are using to answer your research questions.

- Data source : Cars.com
- Data size (2.9 MB)
- Data shape (14420 and 15 columns)
- **Each row represents a single car listing from a dealership**
- Data dictionary

  <img width="249" alt="image" src="https://github.com/user-attachments/assets/9d760765-6348-40f9-a9fa-08f276a3ea31">

- Which variable/column will be your target/label in your ML model?
  Price_usd

## 4. Project Implementation Plan

<img width="557" alt="image" src="https://github.com/user-attachments/assets/cad41f8e-9b98-4881-819f-d907600d9840">


## 5. Exploratory Data Analysis (EDA)

<img width="455" alt="image" src="https://github.com/user-attachments/assets/605ff72d-395f-4b0c-8f64-0683a4492c11">

<img width="455" alt="image" src="https://github.com/user-attachments/assets/42f5c83a-4015-4854-85c9-1252923df9d0">

<img width="430" alt="image" src="https://github.com/user-attachments/assets/b374bb3d-c5f9-4880-a76c-c4358138cda6">

<img width="236" alt="image" src="https://github.com/user-attachments/assets/8176b3b6-8f6f-456c-89f0-cbbb5d460611">

<img width="562" alt="image" src="https://github.com/user-attachments/assets/069b3820-ed7a-4e29-b561-ef6381a5f66e">

<img width="354" alt="image" src="https://github.com/user-attachments/assets/383f2884-9677-4ce8-827d-89ffb7a01917">

<img width="354" alt="image" src="https://github.com/user-attachments/assets/29c803eb-bc77-4b95-882c-ce28a4edfb60">

<img width="374" alt="image" src="https://github.com/user-attachments/assets/d9790877-ef4e-4e33-8301-6b1e24166f28">

<img width="375" alt="image" src="https://github.com/user-attachments/assets/c1b8e0b5-ee67-4b40-9098-f8ce4cd1f833">

<img width="454" alt="image" src="https://github.com/user-attachments/assets/ffb2bff9-d3fb-4336-b186-a98e434dacbd">


## 5. Feature Engineering
- Impute Missing Values with Mean in that Category(i.e by Transmission type, fuel type, drive train, age )
- Categorical Feature Encoding
  1. One Hot Encoding - For Linear Based Models
  2. Label Encoding  - For Tree based models


## 5. Model Training 
Initial Attempt
Dataset split : 80 Test – 20 Train
Tree Based Algorithms
Decision Tree - R-squared : 0.6178
Random Forest - R-squared: 0.7904
XGBoost - R-squared: 0.8223
GradientBoost - R-squared: 0.7618
Linear Models
Linear Regression - R-squared: -51310135364.8435
Addressing Linear Models
Multicollinearity in dataset (Age, Year, Dealer)
Non Linear relations (User Reviews and Dealership Rating)
Improvement
Linear Regression - R-squared: - 0.7568
<img width="417" alt="image" src="https://github.com/user-attachments/assets/06a5f476-c67c-405e-817d-dcb61e0ec65d">


## 6. Application of the Trained Models

Develop a web app for people to interact with your trained models. Potential tools for web app development:

- **Streamlit** (recommended for its simplicity and ease to learn)
- Dash
- Flask

## 7. Conclusion

- Summarize your work and its potetial application
- Point out the limitations of your work
- Lessons learned 
- Talk about future research direction

## 8. References 

- (https://brightdata.com/blog/how-tos/using-selenium-for-web-scraping 
)

