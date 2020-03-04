#Kevin Lee assign 7 

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy.random as random

file = "all_month.csv"
#does not work due to empty cells 
# data1 = np.genfromtxt(file, unpack= True, skip_header=1)


#time	latitude	longitude	depth	mag	magType	nst	gap	dmin	
#rms	net	id	updated	place	type	horizontalError	depthError	
#magError	magNst	status	locationSource	magSource

data3  = pd.read_csv(file,parse_dates=True, header=0)

# Generate a histogram of earthquake magnitude, using a bin 
# width of 1 and a range of 0 to 10. (hint: how does the selction of bin 
# 	size and range affect what the historgram displays? what does the 
# 	histogram suggest about the distribution of the data?)

bins = [0,1,2,3,4,5,6,7,8,9]
first=data3['mag'].plot.hist(bins=bins,alpha=0.5)
plt.show(first)

#based on several trials, 6 bins  shows the most.
#With low bins, i.e. 4, 0 to 2 showed the most freqeunt. This also referes to 
#too much information is compressed. 
#The histogram suggests that 1 to 2 magnitude of earth quake is most frequent. 
bins = [0,1,2,3,4,5,6]
second=data3['mag'].plot.hist(bins=bins,alpha=0.5)
plt.show(second)

#plot KDE with same data
kde=data3['mag'].plot.kde(ind=bins)
plt.show(kde)


#plot long and lat info. Must use longitude for x axis, which measures x axis for plotting
#https://desktop.arcgis.com/en/arcmap/10.3/guide-books/map-projections/about-geographic-coordinate-systems.htm
lat = data3['latitude']
long = data3['longitude']
xy=plt.scatter(long, lat)
plt.show(xy)


#CDF plot 
from scipy import stats
from statsmodels import tools
ser=  data3['depth']
data_sort = np.sort(ser)
p = 1. * np.arange(len(ser)) / (len(ser) - 1)
ser[len(ser)] = ser.iloc[-1]
cum_dist = np.linspace(0.,1.,len(ser))
ser_cdf = pd.Series(cum_dist, index=ser)
# cdf=ser_cdf.plot(drawstyle='steps')
cdf= plt.plot(data_sort, p, drawstyle='steps')
plt.show(cdf)
# ecdf =data3['depth'].plot.hist(cumulative=True, histtype='step')
# plt.show(ecdf)



#Generate scatter  mag vs depth 
x = data3['mag']
y = data3['depth']
y = y[:-1]
mag=plt.scatter(x, y)
#low magnitude earth quake happens at shallow depth. 
#however large magnitude, 4 or 5, happened from very deep. 
# plt.figure()
plt.show(mag)



#generate QQ  plot
mag_data = data3['mag'].values.flatten()
from statsmodels.graphics.gofplots import qqplot
qq=qqplot(mag_data, line ='s')
plt.show(qq)