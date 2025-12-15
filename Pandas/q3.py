import pandas as pd

"""   Transformation      """

df2=pd.DataFrame({'name':['A','B','C','D'],'age':[81,10,115,20],'salary':[1000,2000,3000,4000]})

#df2['Group']=df2['age'].map(lambda x:'Young' if x>10 else 'Adult')

"""     

  name  age  Group
0    A    8  Adult
1    B   10  Adult
2    C   15  Young
3    D   20  Young



"""



#df2['salary']=df2['salary'].apply(lambda x:x+500)

"""

  name  age  salary
0    A    8    1500
1    B   10    2500
2    C   15    3500
3    D   20    4500


"""


#df2['salary'] = df2['salary'].where(df2['salary'] > 2000)

#a=df2[df2['salary']>2000]

#df2.rename(columns={'salary':'Employee_Salary'},inplace=True)

#sdf=df2.sort_values(by=['age','salary'],ascending=[True,False])

#print(sdf)




sdf2=df2.sort_index(ascending=False,inplace=True)

print(sdf2)


#print(a)