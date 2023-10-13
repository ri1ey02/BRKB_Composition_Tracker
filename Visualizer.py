#Visualize in pie chart

import matplotlib.pyplot as plt
import seaborn as sns
import BRKB_Composition_Tracker 

#define data
data, labels  = [], []
all_holdings_percentage = BRKB_Composition_Tracker.getData()
for key, value in all_holdings_percentage.items():
    data.append(round(value,2))
    labels.append(key)

#define Seaborn color palette to use
colors = sns.color_palette('pastel')[0:5]

#create pie chart
plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
plt.savefig('output/pie_chart.png')
