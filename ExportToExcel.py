
import pandas as pd
import json

f = open("result.json")

listdict = json.load(f)

for entry in listdict:
  entry['execution_time'] = int(entry['execution_time'])

df = pd.DataFrame.from_dict(listdict)

datatoexcel = pd.ExcelWriter('TestResultSheet.xlsx')

df.to_excel(datatoexcel)

datatoexcel.save()


df_by_algorithm_depth = df.groupby(['algorithm', 'depth']).mean()

datatoexcel2 = pd.ExcelWriter('AlgorithmResultSheet.xlsx')

df_by_algorithm_depth.to_excel(datatoexcel2)

datatoexcel2.save()




