# Analytics Insight in Automotive Industry

This is a web application that provides data analysis useful for manufacturers in automotive industry.
It helps the industrialists to take informed decisions.


### Features:
* #### Data Visualization:
  We applied exploratory data analysis on cars data so as to find different patterns and relations which are represented through various visualization techniques.
* #### Market Price Prediction:
  We generated a machine learning model for predicting the market price of a car with given specifications(Cylinders, Mileage,etc). It helps in fixing the price for the new car model.
* #### Sales Analysis:
  We used a sales dataset(2007-16) to analyze the averge number of sales in various months. This helps us to address the query: "When to launch a new car?"
  We also analyzed the overall sales of cars so as to find out which company could give the most competetion.

### Technologies Used
* VSCode == 1.67.2
* python == 3.9.4
* Django == 4.0.4

### Python Libraries Used
* numpy
* pandas
* matplotlib
* pickle
* seaborn
* sklearn

### How to install and run project?
* Install VSCode Editor
* Create a virtual environment in VSCode terminal

  `py -3 -m venv .venv`
  
  `.venv\scripts\activate`

* Activate server i.e. virtual environment

  `& /.../.../.venv/Scripts/Activate.ps1`
  
* Clone the project from master branch in the repository and open the folder in VSCode
* Run the server

  `python manage.py runserver`
  
* Open the browser and give local host IP address.
