import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import pandas as pd
import datetime

def graph_data(product, req_day):
    df_brent = pd.read_csv("static/data/brent-daily.csv")
    df_brent['Date'] = pd.to_datetime(df_brent['Date'])
    df_brent['year'], df_brent['month'] = df_brent['Date'].apply(lambda x: x.year), df_brent['Date'].apply(lambda x: x.month)

    df_wti = pd.read_csv("static/data/wti-daily.csv")
    df_wti['Date'] = pd.to_datetime(df_wti['Date'])
    df_wti['year'], df_wti['month'] = df_wti['Date'].apply(lambda x: x.year), df_wti['Date'].apply(lambda x: x.month)

    print("test....................")
    df_murban = pd.read_csv("static/data/OPEC-ORB.csv")
    df_murban['Date'] = pd.to_datetime(df_murban['Date'])
    df_murban['year'], df_murban['month'] = df_murban['Date'].apply(lambda x: x.year), df_murban['Date'].apply(lambda x: x.month)

    now = datetime.datetime.now()
    current_year = now.year

    if product =="brent crude" and req_day =="last year":
        df_brent = df_brent[df_brent['year'] == current_year-1]
        return df_brent
    elif product =="wti crude" and req_day =="last year":
        df_wti = df_wti[df_wti['year'] == current_year-1]
        return df_wti
    elif product =="murban" and req_day =="last year":
        df_murban = df_murban[df_murban['year'] == current_year - 1]
        return df_murban
    elif product =="brent crude wti crude" and req_day =="last year":
        df_brent = df_brent[df_brent['year'] == current_year-1]
        df_wti = df_wti[df_wti['year'] == current_year-1]
        return df_brent, df_wti
    