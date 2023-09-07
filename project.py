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
def maths():
    with open("/mathstoper.txt","w") as mt:
        mathssorted=df_sorted.sort_values(by='maths',ascending=False)
        mathstopper=mathssorted.head(3)
        selected_columns = mathstopper[['name', 'maths']]
        mt.write('Maths\n')
        selected_columns.to_csv(mt, sep='\t', index=False)
def english():
    with open("/englishtoper.txt","w") as et:
        englishsorted=df_sorted.sort_values(by='english',ascending=False)
        englishtopper=englishsorted.head(3)
        selected_columns = englishtopper[['name', 'english']]
        et.write('English\n')
        selected_columns.to_csv(et, sep='\t', index=False)
def science():
    with open("/sciencetoper.txt","w") as st:
        sciencesorted=df_sorted.sort_values(by='science',ascending=False)
        sciencetopper=sciencesorted.head(3)
        selected_columns = sciencetopper[['name', 'science']]
        st.write('Science\n')
        selected_columns.to_csv(st, sep='\t', index=False)
def total():
    with open("/totaltoper.txt","w") as tt:
        totalsorted=df_sorted.sort_values(by='total',ascending=False)
        totaltopper=totalsorted.head(3)
        selected_columns = totaltopper[['name', 'total']]
        tt.write('Total\n')
        selected_columns.to_csv(tt, sep='\t', index=False)
english()
science()
maths()
total()