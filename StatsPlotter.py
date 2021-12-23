'''*************************************************
            Online Python Compiler
    Code, Compile & Run Python program online
Library: NumPy, Matplotlib, Pandas, SciPy, Seaborn
***************************************************'''

#Example - plotting histogram using matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import json

f = open("result.json")

listdict = json.load(f)

for entry in listdict:
  entry['execution_time'] = int(entry['execution_time'])

df = pd.DataFrame.from_dict(listdict)
df_15_19 = df.query("depth > 14 and depth < 19")
print(df.head())

sns.set()
#-----------------------------------
def lable_style(value):
  value = int(value)
  if(value/1000000>=1):
    return f"{int(value/1000000)} M"
  elif(value/1000>=1):
    return f"{int(value/1000)}k"
  return f"{value}"

g = sns.catplot(x="depth", y="nodes_visited", data=df_15_19, kind="bar", hue="algorithm", hue_order=["MinMax", "Smart", "AlphaBeta", "Fastest"], aspect=2)
ax = g.facet_axis(0,0)
for p in ax.patches:
    ax.text(p.get_x() , 
            p.get_height() * 1.02, 
           '{0}'.format(lable_style(p.get_height())),   #Used to format it K representation
            color='black', 
            rotation='horizontal', 
            size='medium')
ax.set(xlabel="N", ylabel="Number of visited nodes (Million nodes)")
#---------------------------------------
def lable_millis(value):
  value = value/1000
  return f"{'{:.1f}'.format(value)}s"

g = sns.catplot(x="depth", y="execution_time", data=df_15_19, kind="bar", hue="algorithm", hue_order=["MinMax", "Smart", "AlphaBeta", "Fastest"], aspect=2)
ax = g.facet_axis(0,0)
for p in ax.patches:
    ax.text(p.get_x() , 
            p.get_height() * 1.02, 
           '{0}'.format(lable_millis(p.get_height())),   #Used to format it K representation
            color='black', 
            rotation='horizontal', 
            size='medium')
ax.set(xlabel="N", ylabel="Execution time (Milliseconds)")
#-----------------------------------------



g.set()
#sns.show_values(splot)
plt.show()
#Arr = np.array([45,64,5,22,55,89,59,35,78,42,34,15])
#b = np.array([0,20,40,60,80,100])

#plt.hist(Arr, bins = b, edgecolor='blue') 
#plt.title('Histogram') 
#plt.show()







for entry in listdict:
  entry['execution_time'] = int(entry['execution_time'])

df = pd.DataFrame.from_dict(listdict)
df_15_19 = df.query("depth > 12 and depth < 20")
df_MinMax = df.query("algorithm == 'MinMax'")
print(df.head())

sns.set()

def lable_style(value):
  value = int(value)
  if(value/1000000>=1):
    return f"{int(value/1000000)} M"
  elif(value/1000>=1):
    return f"{int(value/1000)}k"
  return f"{value}"

g = sns.catplot(x="depth", y="nodes_visited", data=df_MinMax, kind="point", hue="algorithm",  aspect=1.5, join=True)
ax = g.facet_axis(0,0)
for p in ax.patches:
    ax.text(p.get_x() , 
            p.get_height() * 1.02, 
           '{0}'.format(lable_style(p.get_height())),   #Used to format it K representation
            color='black', 
            rotation='horizontal', 
            size='medium')
ax.set(xlabel="N", ylabel="Number of visited nodes (Million nodes)",title="Comparison between Fastest and AlphaBeta")




g.set()
#sns.show_values(splot)
plt.show()