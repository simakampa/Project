import pandas as pd

def load_weather_data():
    df = pd.read_csv("weather_data.csv")

    # Convert DATE
    df['DATE'] = pd.to_datetime(df['DATE'])

    # Add year column
    df['year'] = df['DATE'].dt.year

    # Fix PRCP (rainfall)
    df['PRCP'] = df['PRCP'].replace('T', 0)
    df['PRCP'] = pd.to_numeric(df['PRCP'], errors='coerce')

    # Convert numeric columns
    cols = ['TEMP', 'MAX', 'MIN', 'WDSP', 'VISIB']
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Handle missing values
    df = df.ffill()

    return df