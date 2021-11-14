# OCS (Ontario Cannabis Store) Price Estimator: Project Overview
- Implemented Linear, Lasso, and Random Forest Regressors to estimate flower prices on the OCS website to help customers decide which products are worth purchasing.
- Scraped over 300 strains from the OCS website using Python and Selenium.
- Created graphs and extracted statistics to explore relationships among price, grams, and THC/CBD amounts.

## Code and Resources
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
