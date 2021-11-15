# OCS (Ontario Cannabis Store) Price Estimator: Project Overview
- Implemented Linear, Lasso, and Random Forest Regressors to estimate flower prices on the OCS website to help customers decide which products are worth purchasing.
- Scraped over 300 strains from the OCS website using Python and Selenium.
- Created graphs and extracted statistics to explore relationships among price, grams, and THC/CBD amounts.

## Code
__Python:__ 3.7

__Packages:__ pandas, numpy, sklearn, matplotlib, seaborn, selenium

## Webscraping
Scraped over 300 flowers sold on the OCS website. The information obtained for each flower is as follows:
- Name
- Type (Blend, indica, sativa, hybrid)
- Producer
- Brand
- Potency
- Price
- Price per gram
- Grams
- Minimum amount of THC
- Maximum amount of THC
- Minimum amount of CBD
- Maximum amount of CBD

## Data Cleaning
The following changes were made:
- Removed duplicates
- Removed '$' sign from price_per_gram
- Parsed prices into separate rows
- Parsed THC range into separate columns
- Parsed CBD range into separate columns
- Transformed potency levels into numerical values (1-5)
- Converted data type of non-numerical columns to "category"

## Exploratory Data Analysis
Explored the distribution of each variable and correlations among the variables. Below are some highlights:
![](https://github.com/jordanchow1/ocs_strains/blob/main/graphs/1.png)
![](https://github.com/jordanchow1/ocs_strains/blob/main/graphs/2.png)
![](https://github.com/jordanchow1/ocs_strains/blob/main/graphs/5.png)
![](https://github.com/jordanchow1/ocs_strains/blob/main/graphs/6.png)
![](https://github.com/jordanchow1/ocs_strains/blob/main/graphs/7.png)
![](https://github.com/jordanchow1/ocs_strains/blob/main/graphs/3.png)

## Model Building
The non-numerical variables (i.e. Producer, Brand, Type) were first converted to "category" data type. Then, the data were split into train and test sets with a test size of 20%.

Linear, Lasso, and Random Forest Regressors were implemented. To compare model performance, K-Fold Cross Validation was used to compare the average R-squared over all 3 fold (i.e. CV=3). Mean Absolute Error (MAE) was computed to quantify how well each model performed given the test set. Scatterplots of the predicted y values and true y values were created to visualize the discrepancy, where a 45-degree straight would mean the model could predict price with perfect accuracy.

## Model Performance
- __Linear Regression:__ MAE: 8.15
- __Lasso Regression:__ MAE: 7.57
- __Random Forest:__ MAE: 0.85
