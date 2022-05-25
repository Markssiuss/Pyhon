from statistics import mode
from turtle import width
from pandas_datareader import data
import datetime as dt
from bokeh.plotting import figure, show, output_file

start = dt.datetime (2016,3,1)
end = dt.datetime (2016,3,31)
#the name is the stock symbol, in this case google. It has several data source to choose
df = data.DataReader(name = "GOOG", data_source = "yahoo", start = start, end = end)

output_file("FinancialGraph\\Graph.html")
p = figure(x_axis_type = 'datetime', width = 1000, height = 400, sizing_mode ="scale_both" )
p.title = "Candelstick chart"

#This kind of graphs shows info in a diferent way if the stock has won value that day or not, so to paint it we need to know the winning/losing days
#rect => x values, y values (midle value), width (mid day for complete rectangle), height (difference).
hour12 = 12*60*60*1000
dfWin = df[df.Close > df.Open]
dfLoss = df[df.Close < df.Open]

p.segment(df.index, df.Low, df.index, df.High, color = "black")
p.rect(dfWin.index, (dfWin.Open + dfWin.Close)/2, hour12, dfWin.Close - dfWin.Open, fill_color = "green", line_color = "black")
p.rect(dfLoss.index, (dfLoss.Open + dfLoss.Close)/2, hour12, dfLoss.Open - dfLoss.Close, fill_color = "red", line_color = "black")
show(p)
