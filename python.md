**variable:** variable is name that holds data.

integer,string,boolean,list,tuple,dictionary,set.

ex : 

age = 25,height = 176;

name = "abc"

iSBus = true

sofrtware = \[vscode,jupyter,anaconda]

langauges = (Python,Java,HTML,CSS,JS)

dictionary = {"name":XYZ,"age":25}



Rules for variable names:



Must start with a letter or underscore (\_)



Cannot start with a number



Cannot contain spaces



Case-sensitive (age and Age are different)





**Loops**



Loops are used to repeat tasks.



For loop

while loop





**Functions:** Reusable code of blocks.

the function is defined using def keyword.

**types of functionas:**

1.Built-in functions



print()		Prints output

len()		Returns length

type()		Returns data type

range()		Gives a range of numbers

input()		Takes user input

sum()		Adds numbers



2.User defined functions


1.fuctions with no arguments

2.Function with Arguments

3.Function with Arguments and Returns Value

4.Lambda Function

5.Recursive Function




Data cleaning and manipulation



pandas:It is a Python library that helps you work with structured data.



Pandas helps you organize, clean, filter, and analyze data easily.



import pandas as pd

1.df = df.drop\_duplicate()  //to remove duplicate values

2.df = df.drop(column = column\_name)  	//to delete any column from dataset

3.df\["column\_name"] = df\["column\_name"].str.lstrip("...")

&nbsp; df\["column\_name"] = df\["column\_name"].str.rstrip("/")		//to remove unwanted charecters from string we are using methods like 									lstrip() ,rstrip()

&nbsp; 

 df\["column\_name"] = df\["column\_name"].str.strip("123./\_")	// we can remove all the charecters we want to remove we are adding that 								in paranthesis





df\["column\_name"].str.replace('\[^a-zA-Z0-9]',' ')		//this will replace the character except a-z ,A-Z \& 0-9




df\["column\_name"] = df\["column\_name"].str.replace('NaN',' ')	//this is for to remove Nan values from dataset.





df.fillna('')				//this will remove all NaN





df = df,reset\_indexr(drop = True)

