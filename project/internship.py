import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

dataset = pd.read_csv('weatherHistory.csv')
print(dataset.head())
dataset_n = dataset.copy()
col1 = dataset['Formatted Date']
date_list = []
for i in col1:
    string = ''
    for j, x in enumerate(i):
        if j<7:
            string = string + x
        else:
            break
    date_list.append(string)

date_list1 = []
for i in col1:
    string = ''
    for j, x in enumerate(i):
        if j<4:
            string = string + x
        else:
            break
    date_list1.append(string)

date_list2 = []
for i in col1:
    string = ''
    for j,x in enumerate(i):
        if j>4 and j<7:
            string = string + x
        else:
            continue
    date_list2.append(string)
data = dataset.copy()

dataset['Formatted Date'] = date_list
dataset_n['Year'] = date_list1
dataset_n['Month'] = date_list2
print(dataset_n.head())

# temp1 = dataset['Temperature (C)'].where(dataset['Formatted Date'] == '2006-04').mean()
temp2 = dataset['Temperature (C)'].where(dataset['Formatted Date'] == '2007-04').mean()
temp3 = dataset['Temperature (C)'].where(dataset['Formatted Date'] == '2008-04').mean()
temp4 = dataset['Temperature (C)'].where(dataset['Formatted Date'] == '2009-04').mean()
temp5 = dataset['Temperature (C)'].where(dataset['Formatted Date'] == '2010-04').mean()
temp6 = dataset['Temperature (C)'].where(dataset['Formatted Date'] == '2011-04').mean()
temp7 = dataset['Temperature (C)'].where(dataset['Formatted Date'] == '2012-04').mean()
temp8 = dataset['Temperature (C)'].where(dataset['Formatted Date'] == '2013-04').mean()
temp9 = dataset['Temperature (C)'].where(dataset['Formatted Date'] == '2014-04').mean()
temp10 = dataset['Temperature (C)'].where(dataset['Formatted Date'] == '2015-04').mean()
temp11 = dataset['Temperature (C)'].where(dataset['Formatted Date'] == '2016-04').mean()

# temp1 = dataset_n['Humidity'].where(dataset_n['Formatted Date'] == '2006').mean()
temp21 = dataset['Apparent Temperature (C)'].where(dataset['Formatted Date'] == '2007-04').mean()
temp31 = dataset['Apparent Temperature (C)'].where(dataset['Formatted Date'] == '2008-04').mean()
temp41 = dataset['Apparent Temperature (C)'].where(dataset['Formatted Date'] == '2009-04').mean()
temp51 = dataset['Apparent Temperature (C)'].where(dataset['Formatted Date'] == '2010-04').mean()
temp61 = dataset['Apparent Temperature (C)'].where(dataset['Formatted Date'] == '2011-04').mean()
temp71 = dataset['Apparent Temperature (C)'].where(dataset['Formatted Date'] == '2012-04').mean()
temp81 = dataset['Apparent Temperature (C)'].where(dataset['Formatted Date'] == '2013-04').mean()
temp91 = dataset['Apparent Temperature (C)'].where(dataset['Formatted Date'] == '2014-04').mean()
temp101 = dataset['Apparent Temperature (C)'].where(dataset['Formatted Date'] == '2015-04').mean()
temp111 = dataset['Apparent Temperature (C)'].where(dataset['Formatted Date'] == '2016-04').mean()

hum1 = []
wind1 = []
for i in range(1, 10):
    x = str(i)
    filter1 = dataset_n["Year"] == '2007'
    filter2 = dataset_n["Month"] == '0' + x
    hum = dataset_n['Humidity'].where(filter1 & filter2).mean()
    wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
    hum1.append(hum)
    wind1.append(wind)

filter1 = dataset_n["Year"] == '2007'
filter2 = dataset_n["Month"] == '10'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
hum1.append(e)
wind1.append(wind)

filter2 = dataset_n["Month"] == '11'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind1.append(wind)
hum1.append(e)

filter2 = dataset_n["Month"] == '12'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
hum1.append(e)
wind1.append(wind)

hum2 = []
wind2 = []
for i in range(1, 10):
    x = str(i)
    filter1 = dataset_n["Year"] == '2008'
    filter2 = dataset_n["Month"] == '0' + x

    hum = dataset_n['Humidity'].where(filter1 & filter2).mean()
    wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()

    hum2.append(hum)
    wind2.append(wind)
filter1 = dataset_n["Year"] == '2008'
filter2 = dataset_n["Month"] == '10'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
hum2.append(e)
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind2.append(wind)

filter2 = dataset_n["Month"] == '11'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
hum2.append(e)
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind2.append(wind)

filter2 = dataset_n["Month"] == '12'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
hum2.append(e)
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind2.append(wind)

hum3 = []
wind3 = []
for i in range(1, 10):
    x = str(i)
    filter1 = dataset_n["Year"] == '2009'
    filter2 = dataset_n["Month"] == '0' + x
    wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
    hum = dataset_n['Humidity'].where(filter1 & filter2).mean()
    hum3.append(hum)
    wind3.append(wind)

filter1 = dataset_n["Year"] == '2009'
filter2 = dataset_n["Month"] == '10'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
hum3.append(e)
wind3.append(wind)

filter2 = dataset_n["Month"] == '11'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
hum3.append(e)
wind3.append(wind)

filter2 = dataset_n["Month"] == '12'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
hum3.append(e)
wind3.append(wind)

hum4 = []
wind4 = []
for i in range(1, 10):
    x = str(i)
    filter1 = dataset_n["Year"] == '2010'
    filter2 = dataset_n["Month"] == '0' + x

    hum = dataset_n['Humidity'].where(filter1 & filter2).mean()
    wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
    wind4.append(wind)
    hum4.append(hum)

filter1 = dataset_n["Year"] == '2010'
filter2 = dataset_n["Month"] == '10'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
hum4.append(e)
wind4.append(wind)

filter2 = dataset_n["Month"] == '11'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
hum4.append(e)
wind4.append(wind)

filter2 = dataset_n["Month"] == '12'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
hum4.append(e)
wind4.append(wind)

hum5 = []
wind5 = []
for i in range(1, 10):
    x = str(i)
    filter1 = dataset_n["Year"] == '2011'
    filter2 = dataset_n["Month"] == '0' + x

    hum = dataset_n['Humidity'].where(filter1 & filter2).mean()
    wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
    hum5.append(hum)
    wind5.append(wind)

filter1 = dataset_n["Year"] == '2011'
filter2 = dataset_n["Month"] == '10'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
hum5.append(e)
wind5.append(wind)

filter2 = dataset_n["Month"] == '11'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind5.append(wind)
hum5.append(e)

filter2 = dataset_n["Month"] == '12'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind5.append(wind)
hum5.append(e)

hum6 = []
wind6 = []
for i in range(1, 10):
    x = str(i)
    filter1 = dataset_n["Year"] == '2012'
    filter2 = dataset_n["Month"] == '0' + x

    hum = dataset_n['Humidity'].where(filter1 & filter2).mean()
    wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
    wind6.append(wind)
    hum6.append(hum)

filter1 = dataset_n["Year"] == '2012'
filter2 = dataset_n["Month"] == '10'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind6.append(wind)
hum6.append(e)

filter2 = dataset_n["Month"] == '11'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
hum6.append(e)
wind6.append(wind)

filter2 = dataset_n["Month"] == '12'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind6.append(wind)
hum6.append(e)

hum7 = []
wind7 = []
for i in range(1, 10):
    x = str(i)
    filter1 = dataset_n["Year"] == '2013'
    filter2 = dataset_n["Month"] == '0' + x
    hum = dataset_n['Humidity'].where(filter1 & filter2).mean()
    wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
    wind7.append(wind)
    hum7.append(hum)

filter1 = dataset_n["Year"] == '2013'
filter2 = dataset_n["Month"] == '10'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind7.append(wind)
hum7.append(e)

filter2 = dataset_n["Month"] == '11'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind7.append(wind)
hum7.append(e)

filter2 = dataset_n["Month"] == '12'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind7.append(wind)
hum7.append(e)

hum8 = []
wind8 = []
for i in range(1, 10):
    x = str(i)
    filter1 = dataset_n["Year"] == '2014'
    filter2 = dataset_n["Month"] == '0' + x
    hum = dataset_n['Humidity'].where(filter1 & filter2).mean()
    hum8.append(hum)
    wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
    wind8.append(wind)

filter1 = dataset_n["Year"] == '2014'
filter2 = dataset_n["Month"] == '10'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
hum8.append(e)
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind8.append(wind)

filter2 = dataset_n["Month"] == '11'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
hum8.append(e)
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind8.append(wind)

filter2 = dataset_n["Month"] == '12'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
hum8.append(e)
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind8.append(wind)

hum9 = []
wind9 = []
for i in range(1, 10):
    x = str(i)
    filter1 = dataset_n["Year"] == '2015'
    filter2 = dataset_n["Month"] == '0' + x

    hum = dataset_n['Humidity'].where(filter1 & filter2).mean()
    hum9.append(hum)
    wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
    wind9.append(wind)

filter1 = dataset_n["Year"] == '2015'
filter2 = dataset_n["Month"] == '10'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
hum9.append(e)
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind9.append(wind)

filter2 = dataset_n["Month"] == '11'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
hum9.append(e)
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind9.append(wind)

filter2 = dataset_n["Month"] == '12'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
hum9.append(e)
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind9.append(wind)

hum10 = []
wind10 = []
for i in range(1, 10):
    x = str(i)
    filter1 = dataset_n["Year"] == '2016'
    filter2 = dataset_n["Month"] == '0' + x

    hum = dataset_n['Humidity'].where(filter1 & filter2).mean()
    hum10.append(hum)
    wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
    wind10.append(wind)

filter1 = dataset_n["Year"] == '2016'
filter2 = dataset_n["Month"] == '10'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
hum10.append(e)
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind10.append(wind)

filter2 = dataset_n["Month"] == '11'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
hum10.append(e)
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind10.append(wind)

filter2 = dataset_n["Month"] == '12'
e = dataset_n['Humidity'].where(filter1 & filter2).mean()
hum10.append(e)
wind = dataset_n['Wind Speed (km/h)'].where(filter1 & filter2).mean()
wind10.append(wind)

pressure = []
filter4 = dataset_n['Month'] == '10'
filter3 = dataset_n['Year'] == '2007'
pre1 = dataset_n['Pressure (millibars)'].where(filter3 & filter4).mean()
filter3 = dataset_n['Year'] == '2008'
pre2 = dataset_n['Pressure (millibars)'].where(filter3 & filter4).mean()
filter3 = dataset_n['Year'] == '2009'
pre3 = dataset_n['Pressure (millibars)'].where(filter3 & filter4).mean()
filter3 = dataset_n['Year'] == '2010'
pre4 = dataset_n['Pressure (millibars)'].where(filter3 & filter4).mean()
filter3 = dataset_n['Year'] == '2011'
pre5 = dataset_n['Pressure (millibars)'].where(filter3 & filter4).mean()
filter3 = dataset_n['Year'] == '2012'
pre6 = dataset_n['Pressure (millibars)'].where(filter3 & filter4).mean()
filter3 = dataset_n['Year'] == '2013'
pre7 = dataset_n['Pressure (millibars)'].where(filter3 & filter4).mean()
filter3 = dataset_n['Year'] == '2014'
pre8 = dataset_n['Pressure (millibars)'].where(filter3 & filter4).mean()
filter3 = dataset_n['Year'] == '2015'
pre9 = dataset_n['Pressure (millibars)'].where(filter3 & filter4).mean()
filter3 = dataset_n['Year'] == '2016'
pre10 = dataset_n['Pressure (millibars)'].where(filter3 & filter4).mean()

pressure.append(pre1)
pressure.append(pre2)
pressure.append(pre3)
pressure.append(pre4)
pressure.append(pre5)
pressure.append(pre6)
pressure.append(pre7)
pressure.append(pre8)
pressure.append(pre9)
pressure.append(pre10)
# wind = dataset_n['Humidity'].where(filter3).mean()
print(wind)

# print(temp1)
# print(hum1)

temp = [temp2, temp3, temp4, temp5, temp6, temp7, temp8, temp9, temp10, temp11]
tempf = [temp21, temp31, temp41, temp51, temp61, temp71, temp81, temp91, temp101, temp111]
labels = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, temp, width, label='Temperature', color = (0.235, 0.64, 0.52, 0.5))
rects2 = ax.bar(x + width/2, tempf, width, label='Apparent Temperature')

ax.set_ylabel('Temperature')
ax.set_title('Temperature vs. Apparent Temperature for Month of April Year Wise')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()

fig, ax = plt.subplots()
rects3 = ax.bar(x - width/2, pressure, width, label='Pressure')
ax.set_ylabel('Pressure')
ax.set_title('Pressure in the Month of October Year Wise')
ax.set_xticks(x)
ax.set_xticklabels(labels)

plt.show()
print(pressure)

fig = plt.figure(figsize=(14, 8))
monthlist = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.plot(monthlist, hum1, label = '2007', marker = 'o', linewidth = 3)
plt.plot(monthlist, hum2, label = '2008', marker = 'o', linewidth = 3)
plt.plot(monthlist, hum3, label = '2009', marker = 'o', linewidth = 3)
plt.plot(monthlist, hum4, label = '2010', marker = 'o', linewidth = 3)
plt.plot(monthlist, hum5, label = '2011', marker = 'o', linewidth = 3)
plt.plot(monthlist, hum6, label = '2012', marker = 'o', linewidth = 3)
plt.plot(monthlist, hum7, label = '2013', marker = 'o', linewidth = 3)
plt.plot(monthlist, hum8, label = '2014', marker = 'o', linewidth = 3)
plt.plot(monthlist, hum9, label = '2015', marker = 'o', linewidth = 3)
plt.plot(monthlist, hum10, label = '2016', marker = 'o', linewidth = 3)

plt.xlabel('Month')
plt.ylabel('Humidity')
plt.legend(loc='upper left')
plt.xticks(monthlist)
plt.title('Humidity over the Years')
plt.show()

fig = plt.figure(figsize=(14, 8))
monthlist = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.plot(monthlist, wind1, label = '2007', marker = 'o', linewidth = 3)
plt.plot(monthlist, wind2, label = '2008', marker = 'o', linewidth = 3)
plt.plot(monthlist, wind3, label = '2009', marker = 'o', linewidth = 3)
plt.plot(monthlist, wind4, label = '2010', marker = 'o', linewidth = 3)
plt.plot(monthlist, wind5, label = '2011', marker = 'o', linewidth = 3)
plt.plot(monthlist, wind6, label = '2012', marker = 'o', linewidth = 3)
plt.plot(monthlist, wind7, label = '2013', marker = 'o', linewidth = 3)
plt.plot(monthlist, wind8, label = '2014', marker = 'o', linewidth = 3)
plt.plot(monthlist, wind9, label = '2015', marker = 'o', linewidth = 3)
plt.plot(monthlist, wind10, label = '2016', marker = 'o', linewidth = 3)

plt.xlabel('Month')
plt.ylabel('Wind Speed')
plt.legend(loc='upper left')
plt.xticks(monthlist)
plt.title('Wind Speed over the Years')
plt.show()








