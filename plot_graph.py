from GraphData import graph_data
import matplotlib.pyplot as plt
import time
plt.style.use('seaborn-whitegrid')

def plot_graph(prod,last_year):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    product = prod
    if last_year ==" ":
        return("Unable to identify period(i.e. last year) , please specify again")
    if product =="brent crude" and last_year =="last year":
        df_brent = graph_data(product,last_year)
        plt.figure(timestr)
        plt.plot(df_brent["Date"], df_brent["Price"], color='orange')
        plt.axhline(df_brent["Price"].mean(), color='c', linestyle='dashed', linewidth=1.5)
        plt.xticks(rotation=45)
        plt.xlabel('Year')
        plt.ylabel('Price')
        plt.title('Brent Crude Price')
        plt.savefig('static/graph/Brent_plot_'+ timestr +'.jpg',ext='jpg', bbox_inches="tight")
        return("/static/graph/Brent_plot_"+ timestr +'.jpg')

    elif product =="wti crude" and last_year =="last year":
        df_wti = graph_data(product,last_year)
        plt.figure(timestr)
        plt.plot(df_wti["Date"], df_wti["Price"], color='orange')
        plt.axhline(df_wti["Price"].mean(), color='c', linestyle='dashed', linewidth=1.5)
        plt.xticks(rotation=45)
        plt.xlabel('Year')
        plt.ylabel('Price')
        plt.title('WTI Crude Price')
        plt.savefig('static/graph/WTI_plot_'+ timestr +'.jpg',ext='jpg', bbox_inches="tight")
        return("/static/graph/WTI_plot_"+ timestr +'.jpg')

    elif product =="brent crude wti crude" and last_year =="last year":
        df_brent, df_wti = graph_data(product, last_year)
        plt.figure(timestr)
        plt.plot(df_brent["Date"], df_brent["Price"], color='g',label='Brent Crude')
        plt.legend()
        plt.plot(df_wti["Date"], df_wti["Price"], color='orange',label='WTI Crude')
        plt.legend()
        plt.xticks(rotation=45)
        plt.xlabel('Year')
        plt.ylabel('Price')
        plt.title('Brent vs WTI Crude Price')
        plt.savefig('static/graph/BrentvsWTI_plot_'+ timestr +'.jpg',ext='jpg', bbox_inches="tight")
        return("/static/graph/BrentvsWTI_plot_"+ timestr +'.jpg')

    elif product =="murban" and last_year =="last year":
        df_murban = graph_data(product,last_year)
        plt.figure(timestr)
        plt.plot(df_murban["Date"], df_murban["Value"], color='orange')
        plt.axhline(df_murban["Value"].mean(), color='c', linestyle='dashed', linewidth=1.5)
        plt.xticks(rotation=45)
        plt.xlabel('Year')
        plt.ylabel('Price')
        plt.title('Murban Crude Price')
        plt.savefig('static/graph/Murban_plot_'+ timestr +'.jpg',ext='jpg', bbox_inches="tight")
        return("/static/graph/Murban_plot_"+ timestr +'.jpg')



    

    
    
    
