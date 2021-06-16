from os import name
import pandas as pd
import csv
from pandas.core.algorithms import mode
import plotly.graph_objects as go
import statistics as st
import random
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

mean_of_sample1 = st.mean(data)
print('mean:',mean_of_sample1)

def random_set_of_mean(counter):
    data_set = []

    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)

    mean = st.mean(data_set)
    return mean

    
mean_list = []
for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

m = st.mean(mean_list)

fig = ff.create_distplot([mean_list],['reading_time'],show_hist = False )
fig.add_trace(go.Scatter(x = [m,m],y = [0,0.17],mode = 'lines',name = 'mean'))
fig.add_trace(go.Scatter(x = [mean_of_sample1,mean_of_sample1],y = [0,0.17],mode = 'lines',name = 'mean'))
fig.show()