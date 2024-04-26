"""
QUESTION:How do you read data from a CSV file into a DataFrame using Pandas?
SOLUTION:You can use the pd.read_csv() function in Pandas to read data from a CSV file into a DataFrame. 
    EXAMPLE 1,EXAMPLE2
"""
def program1():
    import pandas as pd
    #df = pd.read_csv(r'D:\Siva\2.My-Learnings\03_Pandas\Classes\student.csv') # Absolute Path
    df = pd.read_csv(r'Classes\student.csv') # Relatively Path
    print("DataFrame:",df) 
    print('*************')
#program1()


def program2():
    import pandas as pd
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [25, 30, 35, 40],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
    df = pd.DataFrame(data)
    # Save DataFrame to Excel file
    df.to_excel('Classes/output.xlsx', index=False)  # Set index=False to exclude DataFrame index from Excel file
    print('File Saved Successfully...')
    print('*************')
#program2()
print('**********************')

"""
QUESTION:What is the difference between loc and iloc in Pandas
SOLUTION:

"""
import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}
df = pd.DataFrame(data, index=['X', 'Y', 'Z'])
print('DataFrame:',df)

# Using loc
print("Using loc:")
print(df.loc['X'])   # Accessing a single row
print(df.loc[['X', 'Z']])  # Accessing multiple rows
print(df.loc[:, 'A'])  # Accessing a single column
print(df.loc[:, ['A', 'C']])  # Accessing multiple columns
print(df.loc['X', 'A'])  # Accessing a single element
print(df.loc[['X', 'Y'], 'B'])  # Accessing multiple rows and a single column

Using iloc
print("\nUsing iloc:")
print(df.iloc[0])   # Accessing a single row
print(df.iloc[[0, 2]])  # Accessing multiple rows
print(df.iloc[:, 0])  # Accessing a single column
print(df.iloc[:, [0, 2]])  # Accessing multiple columns
print(df.iloc[0, 0])  # Accessing a single element
print(df.iloc[[0, 1], 1])  # Accessing multiple rows and a single column


