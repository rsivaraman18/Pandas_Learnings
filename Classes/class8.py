title ='''You can create a DataFrame in Pandas by passing a /ndictionary of lists, a dictionary of arrays, or a list of dictionaries to the pd.DataFrame() constructor.'''
print(title)
 
def pgm1():
    import pandas as pd

    # Dictionary of lists
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [25, 30, 35, 40],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

    # Creating DataFrame
    df = pd.DataFrame(data)
    print("Dictionary of lists")
    print(df)
    print('***************')
  
def pgm2():
    import pandas as pd
    import numpy as np

    # Dictionary of arrays
    data = {'A': np.array([1, 2, 3, 4]),
            'B': np.array([5, 6, 7, 8]),
            'C': np.array([9, 10, 11, 12])}

    # Creating DataFrame
    df = pd.DataFrame(data)
    print("Dictionary of arrays")
    print(df)
    print('***************')
#pgm2()


def pgm3():
    import pandas as pd

    # List of dictionaries
    data = [{'Name': 'Alice', 'Age': 25, 'City': 'New York'},
            {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
            {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'},
            {'Name': 'David', 'Age': 40, 'City': 'Houston'}]

    # Creating DataFrame
    df = pd.DataFrame(data)

    print(df)
 
# pgm3()

programs = [pgm1,pgm2,pgm3]
for program in programs:
    program()
print('Done')

'''


                    Name  Age         City
            0    Alice   25     New York
            1      Bob   30  Los Angeles
            2  Charlie   35      Chicago
            3    David   40      Houston
***************
                Dictionary of arrays
                    A  B   C
                0  1  5   9
                1  2  6  10
                2  3  7  11
                3  4  8  12
***************
                Name  Age       City
        0    Alice   25     New York
        1      Bob   30  Los Angeles
        2  Charlie   35      Chicago
        3    David   40      Houston

'''
