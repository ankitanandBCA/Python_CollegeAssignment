import pandas as pd


df=pd.DataFrame({'id':[1,2,3,4],'name':['A','B','C','D'],'mark':[8,10,15,20]})
df1=pd.DataFrame({'id':[5,6,3,4],'name':['A','B','C','D'],'mark':[18,55,45,50]})


#a=pd.merge(df,df1,on='id')

#a = pd.merge(df, df1, on='id', how='outer')
#a = pd.merge(df, df1, on='id', how='left')




#a=df.join(df1,lsuffix='_left',rsuffix='_right')

#a=pd.concat([df,df1],axis=0,join='outer',ignore_index=False)
#a=pd.concat([df,df1],axis=1,join='outer',ignore_index=False)

#a=pd.concat([df,df1],axis=1,join='inner',ignore_index=False)

#a=pd.concat([df,df1],axis=0,join='inner',ignore_index=False)

#print(a)





