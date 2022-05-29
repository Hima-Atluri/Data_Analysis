import pandas as pd 
import seaborn as sns 
import pickle
from sklearn.model_selection import train_test_split,train_test_split
from sklearn.ensemble import RandomForestRegressor

sns.set(color_codes=True)
# Loading the CSV file into a pandas dataframe.
df = pd.read_csv("cars_test.csv")
df.head(5)
df=df.drop(['Make','Model','Variant','Drivetrain','S.no','Fuel_Type','Body_Type','Type','Ground_Clearance(mm)',
            'Valves_Per_Cylinder','ARAI_Certified_Mileage_for_CNG(km/kg)','Height(mm)','Length(mm)','Width(mm)',
            'Highway_Mileage(km/litre)'], axis=1)

#data clearing by replacing with mean values
for c in df:
    x = df[c].mean()
    df[c].fillna(x, inplace = True)
X = df.drop('Ex-Showroom_Price(Rs.)', axis=1)
y = df['Ex-Showroom_Price(Rs.)']

X = X.to_numpy()
y = y.to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating the Random Forest Regressor Model
rfgm= RandomForestRegressor()
rfgm.fit(X_train, y_train)
pred = rfgm.predict(X_test)
#print("The R2 square value of RandomForest Regressor is :", r2_score(y_test, pred)*100)


# saving model as a pickle
pickle.dump(rfgm, open('project_data_analytics/pp_model.sav','wb'))
