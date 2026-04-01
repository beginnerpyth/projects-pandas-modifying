import pandas as pd
import csv
data={'1':['a','b','c'],
      '2':['d','e','f']}
df=pd.DataFrame(data,index=['a','b','c'])#so with data frame we can chaneg the index 
print(df)
#with orient in default the key is column but you ccan change into index but you need to do DataFrame.from_dict
df1=pd.DataFrame.from_dict(data,orient='index',columns=[1,2,3])#normally orient is column and orient means key
print(df1)
bios=pd.read_csv('bios.csv')
coffee=pd.read_csv('coffee.csv')
print(bios.head(4))
print(coffee.head(5))
#with open('try.csv','w')as e:
##    files=csv.reader(e)
    #files.rea(['total_revenue','product_id'])
coffee['price']=13
print(coffee)
print(coffee[['Units Sold','price']])
g=coffee[['Units Sold','price']]
#see=list(g)
#print(see)
see=list(g.to_dict(orient='records'))
print(see)    

    #print(files['total_revenue'])




    