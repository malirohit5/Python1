import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["Rohit", "Salwa", "Amba", "Rohit", "Salwa"],
    "email": ["rohit@example.com", "salwa@#gmail.com", "amba@@mail.com", "rohit@example.com", "NaN"],
    "age": [23, 25, np.nan, 23, 30]
})

#print("Original Data:")
#print(df)

print("THIS IS THE CORRECT FILE")

df = df.drop_duplicates(subset=['name'])
print(df)

df = df.drop(columns=["name"])
print(df)

print("\n--- Replace 'NaN' String with Actual NaN ---")
df["email"].replace("NaN", np.nan, inplace=True)
print(df)


print("\n--- Remove Actual NaN ---")
df = df.dropna()
print(df)




print("\n Numpy Python Library")

arr = np.array([10, 20, 30, 40])
print(arr)

arr1 = np.array([[1,2,3],[4,5,6],
                [7,8,9],[10,11,12]])
print(arr1)

print(arr1.ndim)   # dimensions
print(arr1.shape)  # rows, columns
print(arr1.size)   # total elements
print(arr1.dtype)  # data type


arr2 = np.ones((3, 3))
print(arr2)
print("Printing range")
arr3 = np.arange(1, 10)
print(arr3)


print("Array  Operatiions")

a = np.array(["A","B"])
b = np.array(["C","D"])
print(a + b)    #Addition

c = np.array([1,2,3])
d = np.array([4,5,6])
print(c * d)    #Multiplication


print(c / d)    #Division


e = np.sqrt(c)

print(e)

np.sum(d)
print(d)


print(arr[-1])
print(arr[0])
print(arr[0:4])
print(arr[1:4:2])