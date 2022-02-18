import pandas as pd
import numpy as np

df_generation = pd.read_csv("data/generation.csv", sep=';')
df_temperature = pd.read_csv("data/temperature.csv", sep=';')
sample_submission = pd.read_csv("data/sample_submission.csv", sep=';')

df_generation = df_generation[df_generation['DateTime'].notna()]

df = pd.merge(df_generation, df_temperature, on='DateTime')

df['Generation'] = df['Generation'].apply(lambda x: float(x.replace(',', '.')))
df['AirTemperature'] = df['AirTemperature'].apply(lambda x: float(x.replace(',', '.')))
df['ComfortTemperature'] = df['ComfortTemperature'].apply(lambda x: float(x.replace(',', '.')))
df['RelativeHumidity'] = df['RelativeHumidity'].apply(lambda x: float(x.replace(',', '.')))
df['WindSpeed'] = df['WindSpeed'].apply(lambda x: float(x.replace(',', '.')))
df['EffectiveCloudCover'] = df['EffectiveCloudCover'].apply(lambda x: float(x.replace(',', '.')))

months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

df['Hour'] = df['DateTime'].apply(lambda x: x.split(' ')[1].split(':')[0]).astype(float)
df['Day'] = df['DateTime'].apply(lambda x: x.split(' ')[0][:2]).astype(float)
df['Month'] = df['DateTime'].apply(lambda x: x.split(' ')[0][2:-4]).map(months).astype(float)
df['Year'] = df['DateTime'].apply(lambda x: x.split(' ')[0][-4:]).astype(float)

sonuc = (df.loc[:, ('AirTemperature', 'Month')].groupby(by=['Month'], as_index=False).mean())
sonuc = df.head()
print(sonuc)
