# Data Science Air Quality Index: Project Overview 

The Air Quality Index (AQI) is an index for reporting air quality on a daily basis. It is a measure of how air pollution affects one's health within a short time period. The purpose of the AQI is to help people know how the local air quality impacts their health. The Environmental Protection Agency (EPA) calculates the AQI for five major air pollutants, for which national air quality standards have been established to safeguard public health.
 
1. Ground-level ozone
2. Particle pollution/particulate matter (PM2.5/pm 10)
3. Carbon Monoxide
4. Sulfur dioxide
5. Nitrogen dioxide

### How is AQI calculated?
 
Different countries use different point scales to report air quality. For instance, the United States uses a 500 point scale, wherein rating between 0 and 50 is considered good. Rating between 301 to 500 range is deemed hazardous. India too follows that the 500 point scale. Every day monitors record concentrations of the major pollutants. These raw measurements are converted into a separate AQI value for each pollutant (ground-level ozone, particle pollution, carbon monoxide, and sulfur dioxide) using standard formulae developed by EPA. The highest of these AQI values are reported as the AQI value for that day.

### Air Quality Index Categories
 
<b>Good (0–50)</b> - Minimal Impact
 
<b>Satisfactory (51–100)</b> - May cause minor breathing difficulties in sensitive people.
 
<b>Moderately polluted (101–200)</b> - May cause breathing difficulties in people with lung disease like asthma, and discomfort to people with heart disease, children and older adults.
 
<b>Poor (201–300)</b> - May cause breathing difficulties in people on prolonged exposure, and discomfort to people with heart disease
 
<b>Very Poor (301–400)</b> - May cause respiratory illness in people on prolonged exposure. Effect may be more pronounced in people with lung and heart diseases.
 
<b>Severe (401-500)</b> - May cause respiratory issues in healthy people, and serious health issues in people with lung/heart disease. Difficulties may be experienced even during light physical activity.
 
### Why is AQI important?
 
Awareness of daily levels of air pollution is important, especially for those suffering from illnesses caused by exposure to air pollution.
 
### Objectives of Air Quality Index (AQI)

Comparing air quality conditions at different locations/cities.
It also helps in identifying faulty standards and inadequate monitoring programmes.
AQI helps in analysing the change in air quality (improvement or degradation).
 
### Who is most at risk from air pollution?
 
People with lung diseases, such as asthma, chronic bronchitis, and emphysema
 
Children, including teenagers
 
Active people of all ages who exercise or work extensively outdoors
 
Some healthy people are more sensitive to ozone
 
# Air-Quality-Prediction
As air pollution is a complex mixture of toxic components with considerable impact on humans, forecasting air pollution concentration emerges as a priority for improving life quality. So with the help of Python tools and some Machine Learning algorithms, we try to predict the air quality. 

## Objective

Here we have access to a large amount of granular data relating to the  concentration of major air pollutants in India and it will be interesting to see if the claim of reduced air pollution is being actually backed by data.

## Types of Air Pollutants

Let's first try and understand the various types of air pollutants in the datasets. On a broader level, these pollutants can be classified as :

![](https://imgur.com/C4q7gwX.png)

* **Particulate matter (PM2.5 and PM10)**>
Particulate matter is a mix of solids and liquids, including carbon, complex organic chemicals, sulphates, nitrates, mineral dust, and water suspended in the air. PM varies in size. Some particles, such as dust, soot, dirt or smoke are large or dark enough to be seen with the naked eye. But the most damaging particles are the smaller particles, known as PM10 and PM2.5.[Source](https://www.blf.org.uk/support-for-you/air-pollution/types). The following diagram will help to understand the concept more concretely.

* **Nitrogen Oxides** (NO, NO<sub>2</sub>, NO<sub>x</sub>)>
Nitrogen oxides are a group of seven gases and compounds composed of nitrogen and oxygen, sometimes collectively known as NOx gases.The two most common and hazardous oxides of nitrogen are nitric oxide(NO) and nitrogen dioxide(NO<sub>2</sub>). NO<sub>2</sub> primarily gets in the air from the burning of fuel. NO<sub>2</sub> forms from emissions from cars, trucks and buses, power plants, and off-road equipment.

* **Sulphur Dioxide**(SO<sub>2</sub>)>
Sulfur dioxide, or SO<sub>2</sub> is a colorless gas with a strong odor, similar to a just-struck match. It is formed when fuel containing sulfur, such as coal and oil, is burned, creating air pollution.

* **Carbon Monoxide**(CO)>
Carbon monoxide is a colorless, highly poisonous gas. Under pressure, it becomes a liquid. It is produced by burning gasoline, natural gas, charcoal, wood, and other fuels.

* **Benzene, Toluene and Xylene** (BTX)>
Benzene, toluene, xylene, and formaldehyde are well-known indoor air pollutants, especially after house decoration. They are also common pollutants in the working places of the plastic industry, chemical industry, and leather industry

* **Ammonia**( NH<sub>3</sub>)>
[Ammonia pollution](https://en.wikipedia.org/wiki/Ammonia_pollution) is pollution by the chemical ammonia (NH3) – a compound of nitrogen and hydrogen which is a byproduct of agriculture and industry.

* **Ozone**(O<sub>3</sub>)>
[Ground-level ozone](https://www.canada.ca/en/environment-climate-change/services/air-pollution/pollutants/common-contaminants/ground-level-ozone.html) is a colorless and highly irritating gas that forms just above the earth's surface. It is called a "secondary" pollutant because it is produced when two primary pollutants react in sunlight and stagnant air. These two primary pollutants are nitrogen oxides (NOx) and volatile organic compounds (VOCs).

## Methodology

In this notebook, the analysis has been done in two parts:

**Analysis of the pollution level in India, over the years - from 2015 to 2020**
This will a holistic view of how the pollutant levels have been rising in India and what is the current situation.

**Effect of Locksown on the Pollution level in India**
Here we shall examine the pollution level in India before and after the first stage of Lockdown.

Also we shall compare the pollution level around the same months in 2019, to see the the difference, if any.

Additionally we could also examine the difference between the the current dates and the winter months(October, November) of 2019 when the pollution levels are generally the highest in Northern parts of India.

Analyzing data under these different categories should give us a fair idea of the effect of Lockdown on the Indian pollution level.

## Context

Air is what keeps humans alive. Monitoring it and understanding its quality is of immense importance to our well-being.

## Content

The dataset contains air quality data and AQI (Air Quality Index) on  daily level across multiple cities in India.

## Cities

Ahmedabad, Aizawl, Amaravati, Amritsar, Bengaluru, Bhopal, Brajrajnagar, Chandigarh, Chennai, Coimbatore, Delhi, Ernakulam, Gurugram, Guwahati, Hyderabad, Jaipur, Jorapokhar, Kochi, Kolkata, Lucknow, Mumbai, Patna, Shillong, Talcher, Thiruvananthapuram, Visakhapatnam


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

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included.

## Data Collection:

The data has been made publicly available by the Central Pollution Control Board: https://cpcb.nic.in/ which is the official portal of Government of India. They also have a real-time monitoring app: https://app.cpcbccr.com/AQI_India/

## Data Cleaning

After scraping the data, I needed to clean it up so that it was usable for our model. I fill the missing values using median, because the distribution of data is skewed.

## Data Preprocessing

In this stage, I looked at the distribution of data and find that distribution of each feature is skewed. If we feed this skewed data to the machine learning model, the model will learn the skewed data that will give us high error rate and it also affects the accuracy of the model. So I have converted those skewed distribution into normal distribution.

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

First, I split the data into train and tests sets with a test size of 20%.   

I tried  different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried different models:
*	**Linear Regressor** 
*	**CatBoost Regressor** 
*	**Random Forest Regressor** 
* **XGB Regressor** 
* **AdaBoost Regressor** 

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**AdaBoost Regressor** : MAE = 0.4
*	**Linear Regressor**: MAE = 0.3
*	**CatBoost Regressor**: MAE = 0.2

## Model Deployement
In this step, I built a django application to deploy the machine learning model that was hosted on a local webserver. The application endpoint takes in a request with a list of values from a interface  listing and returns an estimated AQI. 

<h3>Happy Coding ✌</h3>
