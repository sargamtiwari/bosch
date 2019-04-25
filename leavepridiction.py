# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:14:42 2019

@author: TWS1KOR
    """
from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
  import pandas as pd
  #import matplotlib.pyplot as plt
    
    #PRIDICTION INTERNS
  dfinterndata=pd.read_csv('leave_predic.csv',sep=',', parse_dates=['Month'],index_col='Month')
    #dfdepartmenthead=pd.read_csv('data for Add in\Department_head.csv',sep=',', parse_dates=['YEAR'],index_col='YEAR')
    
    #interns resource pridiction
  print(dfinterndata)
  #yt=dfinterndata[33:]
  from sklearn.preprocessing import StandardScaler 
  scaler = StandardScaler()
    
  dfgpmscale=scaler.fit_transform(dfinterndata)
    #dfasp=scaler.fit_transform(dfasp)
  colgp=dfinterndata.columns
  traingp =dfgpmscale[:33]
  #validgp =dfgpmscale[33:]


  print(colgp)
  from statsmodels.tsa.vector_ar.var_model import VAR

  model = VAR(endog=traingp)
  model_fit = model.fit()
  prediction = model_fit.forecast(model_fit.y, steps=12)
  predgroup= scaler.inverse_transform(prediction)
  pred_group_manager= pd.DataFrame(index=range(0,len(predgroup)),columns=[colgp])  











#pred_group_manager= pd.DataFrame(index=range(0,len(predgroup)),columns=[colgp])  
  for j in range(0,3):
    for i in range(0, len(predgroup)):
     if predgroup[i][j]<0:
           predgroup[i][j]=0; 
     pred_group_manager.iloc[i][j] =round( predgroup[i][j]) 
     









   
#print(pred_group_manager.iloc[0][1])        
  res=[]
  for j in range(0,3):
   temp=[]
   for i in range(0,len( pred_group_manager)) :
     if  int(pred_group_manager.iloc[i][j])==1:
           temp.append('Yes')
     if int(pred_group_manager.iloc[i][j])==0:
           temp.append('No')
    
   res.append(temp) 
   



  data = pd.DataFrame(res)
  data = data.transpose()
  data.columns = colgp
  return (data.to_json())
if __name__=='__main__' :
    app.run(host='0.0.0.0')







