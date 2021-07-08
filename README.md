# Data Science Air Quality Index: Project Overview 



Methods and Data Sources:
The research area is on Delhi, India. In the first stage, we analyze the spatial and temporal characteristics of air pollution of the 5 cities while in the second stage the Granger causality test is applied to investigate whether air pollution of a city is affected by its neighbors, and vice versa.

For now we have used PM2.5 feature for this analysis. One aim of this study is to test for causal relationships between air pollution of Delhi and its neighboring cities by means of a time-series econometric method, specifically, Granger causality test. However, the first step is to test if all AQI values are stationary and integrated of the same order. Hence, a unit root test, namely, augmented Dickey Fuller (ADF) test is first introduced, followed by Granger causality test.

# Air-Quality-Prediction
As air pollution is a complex mixture of toxic components with considerable impact on humans, forecasting air pollution concentration emerges as a priority for improving life quality. So with the help of Python tools and some Machine Learning algorithms, we try to predict the air quality. 


## Context
Air is what keeps humans alive. Monitoring it and understanding its quality is of immense importance to our well-being.

## Content
The dataset contains air quality data and AQI (Air Quality Index) on  daily level across multiple cities in India.

## Cities
Ahmedabad, Aizawl, Amaravati, Amritsar, Bengaluru, Bhopal, Brajrajnagar, Chandigarh, Chennai, Coimbatore, Delhi, Ernakulam, Gurugram, Guwahati, Hyderabad, Jaipur, Jorapokhar, Kochi, Kolkata, Lucknow, Mumbai, Patna, Shillong, Talcher, Thiruvananthapuram, Visakhapatnam

## Acknowledgements
The data has been made publicly available by the Central Pollution Control Board: https://cpcb.nic.in/ which is the official portal of Government of India. They also have a real-time monitoring app: https://app.cpcbccr.com/AQI_India/



You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included.

## Code and Resources Used 
**Python Version:** 3.8
**For Web Framework Requirements:**  ```pip install -r requirements.txt``` 

## Install
This project requires Python 3.6 and the following libraries installed:
- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [seaborn](https://seaborn.pydata.org/)

## Data Collection:

The data has been made publicly available by the Central Pollution Control Board: https://cpcb.nic.in/ which is the official portal of Government of India. They also have a real-time monitoring app: https://app.cpcbccr.com/AQI_India/

## Data Cleaning

After scraping the data, I needed to clean it up so that it was usable for our model. I fill the missing values using median, because the distribution of data is skewed.


## Exploratory Data Analysis

I looked at the distributions of the data and the trends between the data, found some following analysis:

1. PM2.5 and PM10 pollution show a seasonal effect, with pollution being higher in winter months as compared to the summer ones.
2. SO2 level has started increasing after 2017, although it had also seen a sudden rise in 2015 also. The same pattern is also reflected in BTX levels also.
3. There is a clear trend that pollution level in India falls in the month of July and August. This might be majorly because monsoon sesason sets in during these months.The BTX levels additionally show a major decline around April.
4. The pollution level then start rising and reach highest levels in winter months. Again, its during these months that a lot of crop residue burning takes place,especially in northern parts of India.
5. SO2 level has started increasing after 2017, although it had also seen a sudden rise in 2015 also. The same pattern is also reflected in BTX levels also.
6. The median values of 2020 are generally less as compared to other years giving us a sense that there might be a reduction on pollution lately.
7. Patna, Delhi , Ahmedabad and Kolkata seem to top the charts. Ahmedabad has maximum concenterations of NO2,SO2 as well as CO levels.


## Model Building 

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Random Forest** : MAE = 11.22
*	**Linear Regression**: MAE = 18.86
*	**Ridge Regression**: MAE = 19.67

## Deployement
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 


