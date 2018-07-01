#ASSIGNMENT 20(PANDAS):
#Question 1: Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.
import pandas as pd
data={'name':['shreya indoliya'],'age':[21],'mailid':['shreya123@gmail.com'],'phoneno':['8126643205']}
df=pd.DataFrame(data)
#print(df)

#Question 2: Import the data and print the following :
#a.) First 5 rows of Dataframe
#b.) First 10 rows of the Dataframe
#c.) find basic statistics on the particular dataset.
#d.) Find the last 5 rows of the dataframe
#e.) Extract the 2nd column and find basic statistics on it.
df1=pd.read_csv('C:/Users/Simran/PycharmProjects/untitled/venv/weather.csv')
print(df1)
print(df1.head(5))
print(df1.head(10))
print(df1.describe())
print((df1.tail()))
print(df1['Location'].describe())