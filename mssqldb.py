import matplotlib.pyplot as plt
import time
import pandas as pd
plt.style.use('seaborn-whitegrid')

def fetch_data(product, actual_planned, req_day):
    import pyodbc

    from datetime import date, timedelta
    conn = pyodbc.connect(r'Driver={SQL Server};Server=10.12.71.63,3102; Database=PanoramaLake; Trusted_Connection=yes;')

    if product in ["c2 agp"]:
        product = "C2 AGP"
        unit = "Tons"
    elif product in ["c3 agp"]:
        product = "C3 AGP"
        unit = "Tons"
    elif product in ["c3 lng"]:
        product = "C3 LNG"
        unit = "Tons"
    elif product in ["c4 agp"]:
        product = "C4 AGP"
        unit = "Tons"
    elif product in ["c4 lng"]:
        product = "C4 LNG"
        unit = "Tons"
    elif product in ["c5 lng"]:
        product = "C5 LNG"
        unit = "Tons"
    elif product in ["c5+ agp","c5 plus agp"]:
        product = "C5+ AGP"
        unit = "Tons"
    elif product in ["condensate"]:
        product = "Condensate"
        unit = "Barrels"
    elif product in ["das"]:
        product = "Das"
        unit = "Barrels"
    elif product in ["ethane"]:
        product = "Ethane"
        unit = "Tons"
    elif product in ["ethylene"]:
        product = "Ethylene"
        unit = "Tons"
    elif product in ["ethylene export"]:
        product = "Ethylene Export"
        unit = "Tons"
    elif product in ["fsopr"]:
        product = "FSOPR"
        unit = "Barrels"
    elif product in ["fuel oil", "fueloil"]:
        product = "FuelOil"
        unit = "Tons"
    elif product in ["gasoil", "gas oil"]:
        product = "Gasoil"
        unit = "Tons"
    elif product in ["gasoline"]:
        product = "Gasoline -91/95/98"
        unit = "Tons"
    elif product in ["granulated sulphur","sulphur"]:
        product = "Granulated Sulphur"
        unit = "Tons"
    elif product in ["injection"]:
        product = "Injection"
        unit = "Standard Cubic Feet"
    elif product in ["jet a1", "jet"]:
        product = "JET A-1"
        unit = "Tons"
    elif product in ["lean gas"]:
        product = "Lean Gas"
        unit = "Standard Cubic Feet"
    elif product in ["lean fertilizer", "leanfertilizer", "fertilizer"]:
        product = "LeanFertilizer"
        unit = "Standard Cubic Feet"
    elif product in ["lean injection","leaninjection"]:
        product = "LeanInjection"
        unit = "Standard Cubic Feet"
    elif product in ["lean other"]:
        product = "LeanOther"
        unit = "Standard Cubic Feet"
    elif product in ["lean sales gas", "leansalesgas"]:
        product = "LeanSalesGas"
        unit = "Standard Cubic Feet"
    elif product in ["liquid sulphur"]:
        product = "Liquid Sulphur"
        unit = "Tons"
    elif product in ["lng"]:
        product = "LNG"
        unit = "Tons"
    elif product in ["lpg"]:
        product = "LPG"
        unit = "Tons"
    elif product in ["crude oil", "murban", "crude"]:
        product = "Murban"
        unit = "Barrels"
    elif product in ["naptha", "naphtha"]:
        product = "Naphtha"
        unit = "Tons"
    elif product in ["polyethylene", "poly ethylene"]:
        product = "PolyEthylene"
        unit = "Tons"
    elif product in ["polypropylene", "poly propylene"]:
        product = "PolyPropylene"
        unit = "Tons"
    elif product in ["proc lean injection", "procleaninjection"]:
        product = "ProcLeanInjection"
        unit = "Standard Cubic Feet"
    elif product in ["propylene"]:
        product = "Propylene"
        unit = "Tons"
    elif product in ["raw gas", "rawgas"]:
        product = "Raw Gas"
        unit = "Standard Cubic Feet"
    elif product in ["sales gas", "natural gas"]:
        product = "Sales Gas (Natural Gas)"
        unit = "Standard Cubic Feet"
    elif product in ["sales agp","salesagp"]:
        product = "SalesAGP"
        unit = "Standard Cubic Feet"
    elif product in ["sales lng","saleslng"]:
        product = "SalesLNG"
        unit = "Tons"
    elif product in ["sales sour gas"]:
        product = "SalesSourGas"
        unit = "Tons"
    elif product in ["upper zakum"]:
        product = "Upper Zakum"
        unit = "Tons"
    elif product in ["urea"]:
        product = "Urea"
        unit = "Tons"

    if req_day[1] == '':
        row_data = single_day_query(product, actual_planned, req_day, conn)
        return row_data, unit
    else:
        row_data = multi_day_query(product, actual_planned, req_day, conn)
        return row_data, unit

def multi_day_query(product, actual_planned, req_day, conn):

    prd = '%s' % product
    result_df = pd.DataFrame()

    if actual_planned == "planned":
        cursor = conn.execute("Select H_Date, Daily_Quota from PR.Production_Data where Material ='" + prd + "' and H_Date between'" + req_day[0] + "' and '" + req_day[1] + "' order by H_Date")
        result_df = pd.DataFrame.from_records(cursor.fetchall(), columns=[Daily_Quota[0] for Daily_Quota in cursor.description])

    elif actual_planned == "actual":
        cursor = conn.execute("Select H_Date, Actual_Value from PR.Production_Data where Material ='" + prd + "' and H_Date between'" + req_day[0] + "' and '" + req_day[1] + "' order by H_Date")
        result_df = pd.DataFrame.from_records(cursor.fetchall(), columns=[Actual_Value[0] for Actual_Value in cursor.description])

    result_df.columns = ['Date', 'Value']
    result_df['Date'] = pd.to_datetime(result_df['Date'], format="%Y-%m-%d")
    return plot_data(result_df)

def single_day_query(product, actual_planned, req_day, conn):
    prd = '%s' % product
    if actual_planned == "planned":
        cursor = conn.execute("Select Daily_Quota from PR.Production_Data where Material ='" + prd + "' and H_Date ='" + req_day[0] + "'")
        try:
            for row in cursor:
                row_data = int(row[0])
                conn.close()
                return row_data
        except:
            pass

    elif actual_planned == "actual":
        cursor = conn.execute("Select Actual_Value from PR.Production_Data where Material ='" + prd + "' and H_Date ='" + req_day[0] + "'")
        try:
            for row in cursor:
                row_data = int(row[0])
                conn.close()
                return row_data
        except:
            pass

def plot_data(df):

    timestr = time.strftime("%Y%m%d-%H%M%S")
    plt.figure(timestr)
    plt.plot(df["Date"], df["Value"], color='orange')
    plt.axhline(df["Value"].mean(), color='c', linestyle='dashed', linewidth=1.5)
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.savefig('static/graph/Murban_plot_' + timestr + '.jpg', ext='jpg', bbox_inches="tight")
    return ("/static/graph/Murban_plot_" + timestr + '.jpg')