# linear algebra
import numpy as np

# data processing
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

import warnings
warnings.filterwarnings(action='ignore')

from sqlalchemy import create_engine

dbstring = "postgresql://monder@127.0.0.1:5432/weatherdb"

connection = create_engine(dbstring).connect()

print("connected to db...")

df = pd.read_sql_table('weather', connection)

print("cleaning data...")

pd.set_option('display.max_columns', None)
df.replace('NaN', np.NaN, inplace=True)

no_yes = {'No': 0, 'Yes': 1}

df['raintoday'] = df['raintoday'].map(no_yes)
df['raintomorrow'] = df['raintomorrow'].map(no_yes)

# find categorical variables
categorical = [var for var in df.columns if df[var].dtype=='O']

# find numerical variables
numerical = [var for var in df.columns if df[var].dtype!='O']

X = df.drop(['raintomorrow'], axis=1)
y = df['raintomorrow']

# display categorical variables
categorical = [col for col in X.columns if X[col].dtypes == 'O']

# display numerical variables
numerical = [col for col in X.columns if X[col].dtypes != 'O']

# impute missing values in X_train and X_test with respective column median in X_train
for col in numerical:
    col_median=X[col].median()
    X[col].fillna(col_median, inplace=True)

# impute missing categorical variables with most frequent value
X['windgustdir'].fillna(X['windgustdir'].mode()[0], inplace=True)
X['winddir9am'].fillna(X['winddir9am'].mode()[0], inplace=True)
X['winddir3pm'].fillna(X['winddir3pm'].mode()[0], inplace=True)
    
# impute missing values in y_train and y_test with respective column median in y_train
y.fillna(y.mode()[0], inplace=True)

def max_value(df, variable, top):
    return np.where(df[variable]>top, top, df[variable])

X['rainfall'] = max_value(X, 'rainfall', 3.2)
X['evaporation'] = max_value(X, 'evaporation', 21.8)
X['windspeed9am'] = max_value(X, 'windspeed9am', 55)
X['windspeed3pm'] = max_value(X, 'windspeed3pm', 57)
    
X_train = pd.concat([X[numerical],
                     pd.get_dummies(X.location), 
                     pd.get_dummies(X.windgustdir),
                     pd.get_dummies(X.winddir9am),
                     pd.get_dummies(X.winddir3pm)], axis=1)

X = X.loc[:, ['humidity3pm', 'sunshine', 'pressure3pm', 'rainfall']]

print("fitting...")

random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X, y)

def classify(hum, sun, press, rain):
    print("in classify")
    arr = np.array([hum, sun, press, rain])
    print(arr)
    arr = arr.astype(np.float64)
    
    query = arr.reshape(1, -1)
    prediction = random_forest.predict(query)[0]
    
    return prediction