#MACHINE LEARNING ALGORITHM(Linear Regression)

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import statsmodels.formula.api as sm

from sklearn.model_selection import train_test_split
from sklearn import metrics

House_Data=pd.read_csv("House_Data.csv",parse_dates=["date"])
House_Data["date"]=House_Data["date"].astype("category")

House_Data["sqft_living"].value_counts()
mean=House_Data["sqft_living"].mean()

sd=House_Data["sqft_living"].std()
def last_list(a):
    if (a>mean-2*sd)&(a<mean+2*sd):
        return a
    
df=House_Data["sqft_living"].apply(last_list)
df.value_counts()
mask=House_Data["sqft_living"]<=df.max()
mask1=House_Data["sqft_living"]>=df.min()
df=House_Data[mask & mask1]
House_Data=df


House_Data=House_Data.drop(["id","date","sqft_lot","sqft_above","sqft_basement","sqft_lot15"],axis=1)

Train, Test=train_test_split(House_Data,test_size=0.35, random_state=0)

model5=sm.ols('price~bedrooms+bathrooms+sqft_living+condition+floors+waterfront+view+grade+yr_built+yr_renovated+zipcode+lat+long+sqft_living15',data=Train).fit()
model5.summary()

prediction=model5.predict(Test)


#GUI using TKINTER
from tkinter import *
master = Tk()
master.configure(background='light green')
master.title("Home Price Prediction")

Label(master, text="BEDROOMS",bg='black',fg='white').grid(row=0,sticky='ew',padx=15)
Label(master, text="BATHROOMS",bg='black',fg='white').grid(row=1,padx=15,sticky='ew')
Label(master, text="SQFT_LIVING",bg='black',fg='white').grid(row=2,padx=15,sticky='ew')
Label(master, text="CONDITION",bg='black',fg='white').grid(row=3,padx=15,sticky='ew')
Label(master, text="FLOOR",bg='black',fg='white').grid(row=4,padx=15,sticky='ew')
Label(master, text="WATERFRONT",bg='black',fg='white').grid(row=5,padx=15,sticky='ew')
Label(master, text="VIEW",bg='black',fg='white').grid(row=6,padx=15,sticky='ew')
Label(master, text="GRADE",bg='black',fg='white').grid(row=7,padx=15,sticky='ew')
Label(master, text="YR_BUILT",bg='black',fg='white').grid(row=8,padx=15,sticky='ew')
Label(master, text="YR_RENOVATED",bg='black',fg='white').grid(row=9,padx=15,sticky='ew')
Label(master, text="ZIPCODE",bg='black',fg='white').grid(row=10,padx=15,sticky='ew')
Label(master, text="LATITUDE",bg='black',fg='white').grid(row=11,padx=15,sticky='ew')
Label(master, text="LONGITUDE",bg='black',fg='white').grid(row=12,padx=15,sticky='ew')
Label(master, text="SQFT_LIVING15",bg='black',fg='white').grid(row=13,padx=15,sticky='ew')


Label(master, text="Predicted House Value",bg='black',fg='white').grid(row=14,padx=15,sticky='ew')
v1=DoubleVar()
v2=DoubleVar()
v3=DoubleVar()
v4=DoubleVar()
v5=DoubleVar()
v6=DoubleVar()
v7=DoubleVar()
v8=DoubleVar()
v9=DoubleVar()
v10=DoubleVar()
v11=DoubleVar()
v12=DoubleVar()
v13=DoubleVar()
v14=DoubleVar()
v15=DoubleVar()

e1 = Entry(master,textvariable=v1)
e2 = Entry(master,textvariable=v2)
e3 = Entry(master,textvariable=v3)
e4 = Entry(master,textvariable=v4)
e5 = Entry(master,textvariable=v5)
e6 = Entry(master,textvariable=v6)
e7 = Entry(master,textvariable=v7)
e8 = Entry(master,textvariable=v8)
e9 = Entry(master,textvariable=v9)
e10= Entry(master,textvariable=v10)
e11= Entry(master,textvariable=v11)
e12= Entry(master,textvariable=v12)
e13= Entry(master,textvariable=v13)
e14= Entry(master,textvariable=v14)
e15= Entry(master,textvariable=v15)

def findout():
    a=v1.get()
    b=v2.get()
    c=v3.get()
    d=v4.get()
    e=v5.get()
    f=v6.get()
    g=v7.get()
    h=v8.get()
    i=v9.get()
    j=v10.get()
    k=v11.get()
    l=v12.get()
    m=v13.get()
    n=v14.get()
    
    entry=pd.DataFrame([[a,b,c,d,e,f,g,h,i,j,k,l,m,n]])
    
    y_predict =model5.predict(entry)
    v15.set(y_predict)

e1.grid(row=0, column=2,padx=20,pady=10)
e2.grid(row=1, column=2,padx=20,pady=10)
e3.grid(row=2, column=2,padx=20,pady=10)
e4.grid(row=3, column=2,padx=20,pady=10)
e5.grid(row=4, column=2,padx=20,pady=
        10)
e6.grid(row=5, column=2,padx=20,pady=10)
e7.grid(row=6, column=2,padx=20,pady=10)
e8.grid(row=7, column=2,padx=20,pady=10)
e9.grid(row=8, column=2,padx=20,pady=10)
e10.grid(row=9, column=2,padx=20,pady=10)
e11.grid(row=10, column=2,padx=20,pady=10)
e12.grid(row=11, column=2,padx=20,pady=10)
e13.grid(row=12, column=2,padx=20,pady=10)
e14.grid(row=13, column=2,padx=20,pady=10)
e15.grid(row=14, column=2,padx=20,pady=10)


b=Button(master,text="Predict",command=findout,fg='white',bg='green',bd=3,highlightthickness=4)
b.grid(row=15,column=2)
b2=Button(master,text="Quit",command=master.destroy,fg='white',bg='green',bd=3,highlightthickness=4)
b2.grid(row=16,column=2)


master.mainloop( )