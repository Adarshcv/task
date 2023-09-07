import csv
import pandas as pd
df=pd.read_csv('file.csv')
df_sorted=df.sort_values(by='name')
mm=list(df_sorted['maths'])
em=list(df_sorted['english'])
sm=list(df_sorted['science'])
tm=[]
for i in range(len(mm)):
    tm.append(mm[i]+em[i]+sm[i])
df_sorted['total']=tm
df_sorted.to_csv("newmark.csv")
def topper(x,z):
    y=int(z)
    with open(x+".txt","w") as mt:
        marksorted=df_sorted.sort_values(by=x,ascending=False)
        topper=marksorted.head(y)
        selected_columns = topper[['name', x]]
        mt.write(x+'\n')
        selected_columns.to_csv(mt, sep='\t', index=False)
n=input("Enter the no of toppers you want:")
topper('english',n)
topper('maths',n)
topper('science',n)
topper('total',n)