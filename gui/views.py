from django.shortcuts import render

import matplotlib
from matplotlib.ft2font import HORIZONTAL
import matplotlib.pyplot as plt
matplotlib.use('Agg')

import os
import pickle
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import warnings
warnings.filterwarnings("ignore")


context={}

def get_dv():
    
        df = pd.read_csv("cars_test.csv")
        
        plt.clf()

        #plotting subplots for frequencies
        plt.figure()
        plt.subplot(1,2,1)
        plt1 = df['Fuel_Type'].value_counts().plot(figsize=(8,12),kind='bar')
        plt.title('Fuel Type Histogram')
        plt.xticks(rotation=HORIZONTAL)
        plt1.set(xlabel = 'Fuel Type', ylabel='Frequency of fuel type')

        plt.subplot(1,2,2)
        plt1 = df['Type'].value_counts().plot(figsize=(8,12),kind='bar')
        plt.title('Type Histogram')
        plt.xticks(rotation=HORIZONTAL)
        plt1.set(xlabel = 'Type', ylabel='Frequency of type')

        plt1.ticklabel_format(style='plain',axis="y")
        plt.savefig(os.path.join('static/pic2.png'),bbox_inches='tight')
        
        #graph for type vs average price
        df1 = pd.DataFrame(df.groupby(['Type'])['Ex-Showroom_Price(Rs.)'].mean().sort_values(ascending = False))
        df1.plot.bar(figsize=(8,12))
        plt.title('Type vs Average Price')
        plt.ylabel("Average price")
        plt.xticks(rotation=HORIZONTAL)
        plt.ticklabel_format(style='plain',axis="y")
        plt.savefig(os.path.join('static/pic1.png'),bbox_inches='tight')
        
        #scatter plot for cc vs price
        plt.clf()
        x=df['Displacement(cc)']
        y=df['Ex-Showroom_Price(Rs.)']
        plt.scatter(x,y)
        plt.xlabel("Displacement(cc)")
        plt.ylabel("Price")
        plt.title('CC vs Price')
        plt.ticklabel_format(style='plain',axis="y")
        plt.savefig(os.path.join('static/pic3.png'),bbox_inches='tight')

    
# method for generating predictions
def getPredictions(Displacement, Cylinders, Fuel_Capacity, Doors, Mileage, ARAI_Mileage, kerb_weight, Seating, Gears,Power,Torque):
    
    #load the model for generating predictions
    model = pickle.load(open("pp_model.sav", "rb"))
    l=[[Displacement, Cylinders, Fuel_Capacity, Doors, Mileage, ARAI_Mileage, kerb_weight, Gears,Power,Torque, Seating]]
    a=np.array(l)

    #prediction
    prediction = model.predict(a)
    return prediction[:1]
        
def result(request):

    #taking input from html page
    Displacement = int(request.GET['Displacement'])
    Cylinders = int(request.GET['Cylinders'])
    Fuel_Capacity = int(request.GET['Fuel_Capacity'])
    Doors = int(request.GET['Doors'])
    Mileage = int(request.GET['Mileage'])
    ARAI_Mileage = int(request.GET['ARAI_Mileage'])
    kerb_weight = int(request.GET['kerb_weight'])
    Seating = int(request.GET['Seating'])
    Gears = int(request.GET['Gears'])
    Power = int(request.GET['Power'])
    Torque = int(request.GET['Torque'])

    #returning predictions
    result = getPredictions(Displacement, Cylinders, Fuel_Capacity, Doors, Mileage, ARAI_Mileage, kerb_weight, Seating, Gears,Power,Torque)
    result[0]=int(result[0])
    return render(request, 'predict.html', {'result':result})

def sales_graph():
    cars = pd.read_csv("norway_new_car_sales_by_model.csv",encoding="latin-1")

    #data cleaning
    all_data_na = (cars.isnull().sum() / len(cars)) * 100
    all_data_na = all_data_na.drop(all_data_na[all_data_na == 0].index).sort_values(ascending=False)[:30]
    cars['Make']=cars['Make'].str.replace('\xa0Mercedes-Benz ','Mercedes-Benz ')

    #competition in the market
    makes = cars.groupby(['Make']).count().index
    sizes = cars.groupby(['Make']).count()['Quantity']
    fig, ax = plt.subplots(figsize=(10,10))
    patches,texts,auto_texts=ax.pie(sizes, labels=makes, autopct='%1.1f%%',shadow=False,  startangle=90)
    for text in texts:
        text.set_color('white')
        text.set_size('large')
    ax.axis('equal')  
    sizes
    plt.tight_layout()
    plt.savefig(os.path.join('static/sales1.png'),transparent=True)

    
    #annual analysis
    yearly_total_sales=cars.pivot_table("Quantity",index="Year",aggfunc="sum")
    yearly_total_sales.plot(kind='bar')
    plt.savefig(os.path.join('static/sales2.png'))
      
    plt.clf()

    #monthly analysis
    monthly_total_sales=cars.pivot_table("Quantity",index="Month",columns="Year",aggfunc="sum")
    monthly_total_sales.mean(axis=1).plot.line()
    plt.title("Monthly sales")
    plt.ylabel("Average no. of sales")
    plt.savefig(os.path.join('static/sales3.png'))
    
def home(request):
    return render(request, 'home.html')
    
def predict(request):
    return render(request,'predict.html')

def dv(request):
    get_dv()
    return render(request,'dv.html')

def sales(request):
    sales_graph()
    return render(request,'sales.html')

