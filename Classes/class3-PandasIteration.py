"""ITERATION WITH PANDAS"""
import pandas as pd
 
def pgm1():
    print("Iterating a List and Pandas Series Will give the same Output")
    new_list = ["Idly","Dosa","Vadai","Chappati"]
    for item in new_list:
        print(item)
    print('*******************')
    print()

    """Output:            
            Idly
            Dosa
            Vadai
            Chappati
    """


def pgm2():
    print("Iterating a List and Pandas Series Will give the same Output")
    new_list = ["Idly","Dosa","Vadai","Chappati"]
    new_series = pd.Series(new_list) 
    for tiffen in new_series:
        print(tiffen)
    print('*******************')
    print()

    """Output:            
            Idly
            Dosa
            Vadai
            Chappati
    """



def pgm3():
    print("Iterating a Dictionary we get only key Values")
    tiffen ={  'Morning':['Idly'],
                "Lunch"  :["Rice"],
                "Dinner":["Parroto"],
            }
    df = pd.DataFrame(tiffen)
    print(df)
    for dish in tiffen:          
        print(dish)



def pgm4():
    print("Iterating a Dictionary using Iteritems")
    print('Iter Item is used to Item with the Columns')
    tiffen = {
        'Morning': ['Idly', 'vadai', "Dosa"],
        "Lunch": ["Rice", "Biriyani", "Fried Rice"],
        "Dinner": ["Parroto", "Chappati", "Naan"],
    }
    df = pd.DataFrame(tiffen)
    for time, dishes in df.iteritems():
        print(time)
        print(dishes)

    """OUTPUT 
            Iterating a Dictionary using Iteritems
            Morning
            0     Idly
            1    vadai
            2     Dosa
            Name: Morning, dtype: object

            Lunch
            0          Rice
            1      Biriyani
            2    Fried Rice
            Name: Lunch, dtype: object

            Dinner
            0     Parroto
            1    Chappati
            2        Naan
            Name: Dinner, dtype: object
    """



def pgm5():
    print("Iterating a Dictionary using Iterrows /n Iter Item is used to Iterate  with the Rows")
    tiffen ={  'Morning':['Idly','vadai',"Dosa"],
                "Lunch"  :["Rice","Biriyani","Fried Rice"],
                "Dinner":["Parroto","Chappati","Naan"],
            }
    df = pd.DataFrame(tiffen)
    for time, dishes in df.iterrows():
        print(time)
        print(dishes)

    """OUTPUT
            Iterating a Dictionary
                0
                Morning       Idly
                Lunch         Rice
                Dinner     Parroto
                Name: 0, dtype: object

                1
                Morning       vadai
                Lunch      Biriyani
                Dinner     Chappati
                Name: 1, dtype: object

                2
                Morning          Dosa
                Lunch      Fried Rice
                Dinner           Naan
                Name: 2, dtype: object
    """


#pgm5()

















