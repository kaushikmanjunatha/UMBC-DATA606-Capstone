 
## 1. Title and Author

- USED CAR ANALYTICS

- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Kaushik Manjunatha
- [LinkedIN](https://www.linkedin.com/in/kaushikm97/)
- [Presentation Slides](https://github.com/kaushikmanjunatha/UMBC-DATA606-Capstone/blob/main/docs/Kaushik%20Manjunatha%20Project%20Presentation.pptx)
- Youtube
    
## 2. Background

- *Total Market Value:* $1.6 trillion in the U.S. as of 2023
- *Market Channels :* Dealerships , Private Sales , Online Platforms

*Personal Experience with Used Car Pricing*
- Pricing was overwhelming when searching for a used car.
- No reliable method to verify correct pricing.
- Relied on word of mouth for pricing validation.


*Why does it matter?*
- This project addresses the common challenge of pricing uncertainty for both buyers and sellers.


*Research questions*
1. Prediction Accuracy
Can machine learning models outperform traditional pricing heuristics in accurately predicting used car values, especially in high-demand vehicle categories like electric, Gasoline and hybrid models?
2. Depreciation Analysis
How does the depreciation rate vary across different car makes and models over time?

*Future Scope :*
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

## 4. Exploratory Data Analysis (EDA)

- Perform data exploration using Jupyter Notebook
- You would focus on the target variable and the selected features and drop all other columns.
- produce summary statistics of key variables
- Create visualizations (I recommend using **Plotly Express**)
- Find out if the data require cleansing:
  - Missing values?
  - Duplicate rows? 
- Find out if the data require splitting, merging, pivoting, melting, etc.
- Find out if you need to bring in other data sources to augment your data.
  - For example, population, socioeconomic data from Census may be helpful.
- For textual data, you will pre-process (normalize, remove stopwords, tokenize) them before you can analyze them in predictive analysis/machine learning.
- Make sure the resulting dataset need to be "tidy":
  - each row represent one observation (ideally one unique entity/subject).
  - each columm represents one unique property of that entity. 

## 5. Model Training 

- What models you will be using for predictive analytics?
- How will you train the models?
  - Train vs test split (80/20, 70/30, etc.)
  - Python packages to be used (scikit-learn, NLTK, spaCy, etc.)
  - The development environments (your laptop, Google CoLab, GitHub CodeSpaces, etc.)
- How will you measure and compare the performance of the models?

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

List articles, blogs, and websites that you have referenced or used in your project.
